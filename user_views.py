
from django.shortcuts import render,redirect
from .models import FeedBack,User,BankDetail,Donation
from django.contrib import messages
# views.py
import qrcode
import base64
from io import BytesIO
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def user_edit_profile(request):
   if request.method=="GET":
      user_email=request.session["user_key"]
      user_obj=User.objects.get(email=user_email)
      user_dict={ "user_info":user_obj}
      return render(request,'ngo_app/user/user_edit_profile.html',user_dict)
   if request.method=="POST":
      profile_pic=request.FILES.get("pic")
      user_phone=request.POST["phone"]
      user_name=request.POST["name"]
      user_email=request.session["user_key"]
      user_obj=User.objects.get(email=user_email)
      if profile_pic is not None:
         user_obj.pic_name=profile_pic 
      user_obj.name=user_name
      user_obj.phone=user_phone
      user_obj.save()
      messages.success(request,"Profile updated succesfully")
      return redirect("user_home")
@csrf_exempt  # Only for testing, in production use proper CSRF token headers with fetch
def generate_qr(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        if not amount:
            return JsonResponse({'error': 'Amount is required'}, status=400)

        # You can use your UPI format or just amount text
        qr_data = f"upi://pay?pa=mansisingj68@oksbi&am={amount}&cu=INR"

        img = qrcode.make(qr_data)
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        img_str = base64.b64encode(buffer.getvalue()).decode()
        return JsonResponse({'image': img_str})


def child_education(request):
    if  request.method=="GET":
     return render(request,'ngo_app/user/child.html')

def animal_shelter(request):
    if  request.method=="GET":
     return render(request,'ngo_app/user/animal.html')

def women_employment(request):
    if  request.method=="GET":
     return render(request,'ngo_app/user/women.html')


def bank_details(request):
  if request.method=="GET":
    bank_detail_list=BankDetail.objects.all()
    bank_detail_dict={
      "Bdetails_key":bank_detail_list
    }
    return render(request,"ngo_app/user/bank_details.html",bank_detail_dict) 
  

   

def user_donation(request):
    if  request.method=="GET":
     return render(request,'ngo_app/user/add_donation.html')
    if request.method=="POST":
       email = request.session["user_key"]
       amount = request.POST["amount"]
       aadhaar = request.POST["aadhaar"]
       transaction_id = request.POST["transaction_id"]
       user=User.objects.get(email=email)
       donation = Donation(user=user,amount=amount,aadhaar=aadhaar,transaction_id=transaction_id)
       donation.save()
       messages.success(request,"Thank you for Donation")
       return redirect("add_donation")


    
       


def user_logout(request):
  request.session.flush()# it will kill or destroy the session
  messages.success(request,"Successfully logged out , Thank you🙏")
  return redirect("user_login")

def user_home(request):
    if request.method=="GET":
     ###fetch/get the value from session
     user_email=request.session["user_key"]
     user_obj=User.objects.get(email=user_email)
     ##select* from User where email=user_email
     ###sending object from view to template
     #### create a dictionary and bind object with a key
     #### and then send the dictionary
     user_dict={ "user_info":user_obj}
              
     
     return render(request,'ngo_app/user/user_home.html',user_dict)


def user_login(request):
    if request.method=="GET":
     return render(request,'ngo_app/user/user_login.html')
    if request.method=="POST":
     user_email=request.POST["email"]
     user_password=request.POST["password"]
     userList=User.objects.filter(email=user_email,password=user_password)
    if len(userList)>0:
      # user_object=userList[0]
      request.session["user_key"]=user_email
      #  request.session["user_role"]="user" ###role based authentication
      return redirect("user_home")
    else:
       messages.error(request,"🤷‍♀️Invalid Credentials")
       return redirect("user_login")
     
def user_registration(request):
    if  request.method=="GET":
     return render(request,'ngo_app/user/user_registration.html')
    if request.method=="POST":
       user_name=request.POST["name"]#it will read data from the textbox
       user_password=request.POST["password"]
       user_email=request.POST["email"]
       user_phone=request.POST["phone"]
       user_pic=request.FILES.get("profile-pic")# get method returns none
       #or user_pic=request.Files["profile_pic"]
       registration_obj=User(email=user_email,name=user_name,phone=user_phone,password=user_password,pic_name=user_pic)
       registration_obj.save()#it will store data into database table
       return redirect("user_login")
       
def user_feedback(request):
    if request.method=="GET":
     user_email=request.session["user_key"] # getting email from session
     user_obj=User.objects.get(email=user_email)
     user_dict={"user_detail":user_obj}
     return render(request,'ngo_app/user/user_feedback.html',user_dict)
    if request.method=="POST":
      user_name=request.POST["name"]#it will read data from the textbox
      user_email=request.POST["email"]
      user_rating=request.POST["rating"]
      user_remark=request.POST["remark"]
      user_pic=request.POST["pic_path"]
      feedback_obj=FeedBack(email=user_email,name=user_name,rating=user_rating,remark=user_remark,user_pic=user_pic)
      feedback_obj.save()#it will store data into database table
      messages.success(request,"🙏 thanks for your time🙏")
    #   return render(request,'ngo_app/user/user_home.html')
      return redirect("user_feedback")



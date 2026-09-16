from django.shortcuts import render,HttpResponse
from.models import Contact,FeedBack,Campaign
# Create your views here.
def all_feedback(request):
   ## select * from feedback
   feedback_list= FeedBack.objects.all()
   feedback_dict={
      "feedback_key":feedback_list
     }
   return render(request,"ngo_app/html/all_feedbacks.html",feedback_dict)
def all_campaign(request):
   ## select * from campaign
   campaign_list= Campaign.objects.all()
   campaign_dict={
      "campaign_key":campaign_list
     }
   return render(request,"ngo_app/html/campaign.html",campaign_dict)
def home(request):
    #return HttpResponse("<h1> This is home page</h1>")
    return render(request,'ngo_app/html/index.html')

def about_us(request):
    #return HttpResponse("<h1> This is home page</h1>")
    return render(request,'ngo_app/html/about_us.html')

def contact_us(request):
    if request.method=="GET":
     return render(request,'ngo_app/html/contact_us.html')
    if request.method=="POST":
      user_name=request.POST["name"]#it will read data from the textbox
      user_phone=request.POST["phone"]
      user_email=request.POST["email"]
      user_question=request.POST["question"]
      contact_obj=Contact(name=user_name,email=user_email,phone=user_phone,question=user_question)
      contact_obj.save()#it will store data into database table
      
      return render(request,'ngo_app/html/contact_us.html')


from django.db import models
from django.utils import timezone
# Create your models here.
class FeedBack(models.Model):
    email=models.CharField(max_length=45,primary_key=True)
    name=models.CharField(max_length=55,null=False)
    rating=models.CharField(max_length=5,null=False)
    remark=models.TextField(default="")
    user_pic=models.CharField(max_length=255,default="")
    date=models.DateField(default=timezone.now)
    def _str_(self):
        return self.name

########Contact Table Model#######
class Contact(models.Model):
    email=models.CharField(max_length=45)
    name=models.CharField(max_length=55,null=False)
    phone=models.CharField(max_length=13,null=False)
    question=models.TextField()
    date=models.DateField(default=timezone.now)
    def _str_(self):
        return self.name
#######Registration#########
class User(models.Model):
    email=models.CharField(max_length=60,primary_key=True)
    name=models.CharField(max_length=60,null=False)
    phone=models.CharField(max_length=13,null=False)
    password=models.CharField(max_length=45,null=False)
    pic_name=models.FileField( upload_to="user_pic/" ,default="")
    def _str_(self):
        return self.name# it represents object into string from self means object

class Campaign(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(default="")
    from_date=models.CharField(max_length=10)
    to_date=models.CharField(max_length=10)
    venue=models.TextField(default="")
    pic_name=models.FileField(upload_to="camp_pic/")
    def _str_(self):
        return self.title

class BankDetail(models.Model):
    bank_holder_name=models.CharField(max_length=20)
    upi_number=models.CharField(max_length=20)

class Donation(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    amount = models.CharField(max_length=10,default="")
    aadhaar = models.CharField(max_length=10,default="")
    transaction_id = models.CharField(max_length=10,default="")
    date = models.DateField(default=timezone.now)
    def _str_(self):
        return self.user.name
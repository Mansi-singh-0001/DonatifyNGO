from django.contrib import admin

# Register your models here.
from.models import FeedBack,Contact,User,Campaign,BankDetail
class FeedBack_Admin(admin.ModelAdmin):
    list_display=["name","email","rating","remark","date"]
class Contact_Admin(admin.ModelAdmin):
    list_display=["name","email","phone","date","question"]
class User_Admin(admin.ModelAdmin):
    list_display=["name","email","phone"]
class Campaign_Admin(admin.ModelAdmin):
    list_display=["title","from_date","to_date","venue"]    

admin.site.register(FeedBack,FeedBack_Admin)
admin.site.register(Contact,Contact_Admin)
admin.site.register(User,User_Admin)
admin.site.register(Campaign,Campaign_Admin)
admin.site.register(BankDetail)

admin.site.site_header="DonatifyNGO Admin DashBoard"
admin.site.site_title="DonatifyNGO offers"
admin.site.index_title="NGO portal "


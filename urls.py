from django.urls import path,include
from . import views,user_views
urlpatterns = [
    path("", views.home,name="home"),
    path("about/",views.about_us,name="about_us"),
    path("contact/",views.contact_us,name="contact_us"),
    path("login/",user_views.user_login,name="user_login"),
    path("registration/",user_views.user_registration,name="user_registration",),
    path("feedback/",user_views.user_feedback,name="user_feedback"),
    path("home/",user_views.user_home,name="user_home"),
    path("user_logout/",user_views.user_logout,name="user_logout"),
    path("all_feedback/",views.all_feedback,name="all_feedbacks"),
    path("campaign/",views.all_campaign,name="all_campaign"),
    path("add_donation/",user_views.user_donation,name="add_donation"),
    path("bank_details/",user_views.bank_details,name="bank_details"),
    path("women/",user_views.women_employment,name="women_empoyment"),
    path("child/",user_views.child_education,name="child_education"),
    path("animal/",user_views.animal_shelter,name="animal_shelter"),
    path('generate_qr/', user_views.generate_qr, name='generate_qr'),
    path('user_edit_profile/', user_views.user_edit_profile, name='user_edit_profile'),
    
]
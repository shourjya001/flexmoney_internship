from . import views
# from .views import *
from django.urls import path
urlpatterns=[
    path("",views.home,name="home"),
    path("home/",views.home,name="home"),
    path("contact/",views.contact,name="contact"),
    path("login/",views.login,name="login"),
    path("signup/",views.signup,name="signup"),
    path("logout/",views.logout,name="logout"),
    path("profile/",views.profile,name="profile"),
    path("advertisement/",views.advertisement,name="advertisement"),
    path("instructor/",views.instructor,name="instructor"),
    path("newsletter/",views.newsletter,name="newsletter"),
    path("changepassword/",views.changepassword,name="changepassword"),
    path("resendpass/",views.resendpass,name="resendpass"),
    path("editprofile/",views.editprofile,name="editprofile"),
    path("completepayment/",views.completepayment,name="completepayment"),
]
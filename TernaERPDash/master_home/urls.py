"""
URL configuration for TernaERPDash project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('',views.master_login,name='login'),
    path('home',views.master_home,name='home'),
    path('loggedin_master_home',views.loggedin_master_home,name='loggedin_master_home'),
    path('login',views.master_login,name='login'),
    path('logout/',views.logoutPage,name='logout'),
    path('logout1',views.logoutPage,name='logout1'),
    path('signup',views.signup,name='signup'),
    path('master_login_check',views.master_login_check,name='master_login_check'),
    path('master_signup',views.master_signup,name='master_signup'),
    path('profile_upload',views.profile_upload,name='profile_upload'),
    path('Image_Upload',views.Image_Upload,name='Image_Upload'),
    path('student_master_view',views.student_master_view,name='student_master_view'),
    

]

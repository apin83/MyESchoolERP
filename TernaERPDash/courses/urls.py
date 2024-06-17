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
    path('courses_home',views.courses_home,name='courses_home'),
    path('courses_add',views.courses_add,name='courses_add'),
    path('courses_addition',views.courses_addition,name='courses_addition'),
    path('courses_edit',views.courses_edit,name='courses_edit'),
    path('courses_update',views.courses_update,name='courses_update'),
    path('popup-data', views.popup_data_view, name='popup_data'),
    path('courses_full_details', views.courses_full_details, name='courses_full_details'),

    # path('student_data',views.student_data,name='student_data'),

]

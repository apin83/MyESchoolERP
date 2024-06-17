from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib import messages
from django.db import models
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.decorators.cache import never_cache
from django.views.decorators.http import require_http_methods
from .models import College_Data, Web_User, ProfileImage
from django.http import HttpResponseRedirect
from .forms import CollegeForm, ProfileForm, Web_User_Form, Web_Login_Form
from courses.forms import Courses_Form
from django.urls import reverse
from django.core.management import call_command
from django.core.files.storage import FileSystemStorage
from django.contrib.sessions.models import Session



# Web_User = get_user_model()

def profile_upload(request):
    call_command('clearsessions')
    if request.method == 'POST':
      form=ProfileForm(request.POST,request.FILES)
      
      if form.is_valid():
            form.save()
            # fs=FileSystemStorage()
            # name=fs.save()
            return redirect('/login')
      else:
            print(form.errors)
    else:
        form = ProfileForm()
  
    return render(request, 'profileimage.html',{})   



def Image_Upload(request):
    call_command('clearsessions')
    model = ProfileImage
    form=ProfileForm()
    template_name='profileimage.html'
    uid = request.GET.get('uname')
    print(uid)
    request.session['uname']=uid
    return render(request,
            'profileimage.html',
            {'form': form})
    # return render(request,'profileimage.html')

def college_view(request):
    call_command('clearsessions')
    context ={} 
    context['form']= CollegeForm() 
    return render(request, "home.html", context) 
  # template = loader.get_template('login.html')
  # return HttpResponse(template.render())

   


def collegedata(request):
    call_command('clearsessions')
    mycollegedata=College_Data.objects.all().values()
    template=loader.get_template('index.html')
    context = {
        'mycollegedata' : mycollegedata,
    }
    return HttpResponse(template,render(context,request))
# Create your views here.

@login_required(login_url='login')
@never_cache
def master_home(request):
  call_command('clearsessions')
  uname=request.GET.get('uname')
  session_key = request.session.session_key
  print(session_key)
  request.session['pass_key']=session_key
  # fullname=request.GET.get('fullname')
  mycollegedata=College_Data.objects.all()
  myuserdata=Web_User.objects.filter(username=uname).values()
  profileimg=ProfileImage.objects.all()
  # imgpath=ProfileImage.objects.filter(user.username==uname)
  print(profileimg)

  if len(profileimg)>0:
      for pi in profileimg:
          if pi.user.username==uname:
            print(pi.path, pi.user.username)
            imgpath=pi.path
            break
          else:
            imgpath="images/default.jpg"
  else:
      imgpath="images/default.jpg"

  uname=request.session['username']
  context = {
      'mycollegedata' : mycollegedata,
      'uname' : uname,
      'myuserdata' : myuserdata,
      'profile_picture' : profileimg,
      'imgpath': imgpath
        }
  template = loader.get_template('index.html')
  return HttpResponse(template.render(request=request,context=context))
 
 
def loggedin_master_home(request):
    call_command('clearsessions')
    uid=request.session.get('username', 'Invalid_User')
    if uid=='Invalid_User':
        print('Session Expired!!!')
        return redirect(request=request, to='/login')
    else:
        request.session['username']=uid
        print(uid)
        url_home = '/home' + '?uname=' + uid
        return redirect(request=request, to=url_home)




def master_login(request):
  call_command('clearsessions')
  form=Web_Login_Form()
  form.method='POST'
  return render(request,
                'login.html',
                {'form':form}
                )
  # template = loader.get_template('login.html')
  # return HttpResponse(template.render())


@csrf_exempt 
def logoutPage(request):
  call_command('clearsessions')
  print("logout called view!!!")

  if 'username' in request.session:
      del request.session['username']
  logout(request)
  template = loader.get_template('logout.html')
  return HttpResponse(template.render(request=request))


def signup(request):
  call_command('clearsessions')
  # model = Web_User
  form=Web_User_Form()
  form.method='POST'
  # template_name='signup.html'
  # uid = request.POST.get('userName')
  # passwd = request.POST.get('password')
  # request.session['username']=uid
  return render(request,
            'signup.html',
            {'form': form})
  # template = loader.get_template('signup.html')
  # return HttpResponse(template.render())

def createuser_view(request):
    call_command('clearsessions')
    uname = request.POST.get('userName')
    upasswd = request.POST.get('password')
    utype = request.POST.get('usertype')
    uemail = request.POST.get('useremail')
    ucontact = request.POST.get('usercontact')
    uisactive = request.POST.get('userisactive')
    # user = User.objects.create_user(request,username=uname,password=upasswd,usertype=utype,
    #                                 useremail=uemail, usercontact=ucontact, userisactive=uisactive)
    user = User.objects.create_user(username=uname, password=upasswd, useremail=uemail)
    user.save()
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

@csrf_exempt   
def master_signup(request):
    call_command('clearsessions')
    
    if request.method=='POST':
        form=Web_User_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
     
        print('User Created Successfully!!!')
        request.session['uname']=request.POST.get('username')
        uid=request.POST.get('username')
        # return redirect(request=request, to='/Image_Upload?uname=' + uid)
        return redirect(request=request, to='login')
    else:
        return redirect(request=request, to='/signup')
        
        # template = loader.get_template('profileimage.html')
        # return HttpResponse(template.render())



@csrf_exempt
@never_cache
def master_login_check(request):  
  call_command('clearsessions')
  form=Web_Login_Form(request.POST)
  if request.method == 'POST':
        uid = request.POST.get('username')
        passwd = request.POST.get('password')
        # uid=form.cleaned_data['username']
        # passwd=form.cleaned_data['password']
       
      
        user = authenticate(request=request, username=uid, password=passwd)
        if user is not None:
            login(request, user)
            mycollegedata=College_Data.objects.all().values()
            request.session['username']=uid
            url_home = '/home' + '?uname=' + uid
          
            return redirect(request=request, to=url_home)  # Redirect to your home page
        else:
            # Handle invalid login
            return render(request, 'login.html', {'error': 'Invalid login credentials'})
  else:
        return render(request, 'login.html',  {'error': 'no'})
        # template = loader.get_template('login.html')
        # return HttpResponse(template.render())

@login_required(login_url='login')
def student_master_view(request):
    call_command('clearsessions')
    return render(request,'studentdata.html')



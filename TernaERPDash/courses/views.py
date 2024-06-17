from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.http import HttpResponse, JsonResponse, Http404
from .forms import Courses_Form, Courses_Form_Edit
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.core.management import call_command
from .models import CoursePrimary


@csrf_exempt 
def popup_data_view(request):
    call_command('clearsessions')
    # Fetch your data here, this is just a placeholder
    cid=request.GET.get('cid')
    print(cid)
    coursedetails=CoursePrimary.objects.filter(courseid=cid).values()
   #  for cd in coursedetails:
   #     c=cd.courseid
   #     course_name=cd.course_name

    context = {
       'coursedetails' : coursedetails,
    }
   #  return redirect(request=request, context=context, to='courses_full_details.html')
    template = loader.get_template('courses_home.html')
    return HttpResponse(template.render(request=request,context=context))
  
   #  return JsonResponse(data)

@csrf_exempt 
def courses_full_details(request):
    call_command('clearsessions')
    return render(request,
                'courses_full_details.html',
                )
   #  return HttpResponse(request=request, to='courses_full_details.html')

  

def courses_home(request):
  call_command('clearsessions')
  if 'username' not in request.session:
     print('key expired!!!') 
     return redirect('logout/')
  else:
     print(request.session['pass_key'])
     coursesdata=CoursePrimary.objects.all()
     course_form=Courses_Form()
     course_form.method='POST'
     uname=request.session['username']
     context = {
        'coursesdata' : coursesdata,
        'course_form':course_form,
        'uname' : uname,
     }
     template = loader.get_template('courses_home.html')
     return HttpResponse(template.render(request=request,context=context))


@csrf_exempt 
def courses_edit(request):
    call_command('clearsessions')
    cid=request.GET.get('cid')
    print(cid)
    course_obj=CoursePrimary.objects.get(courseid=cid)
    print(course_obj)
    form=Courses_Form_Edit(instance=course_obj)
    form.method='POST'

    context = {
       'course_form' : form,
       'cid' : cid,
    }
   #  return redirect(request=request, context=context, to='courses_full_details.html')
    template = loader.get_template('courses_update.html')
    return HttpResponse(template.render(request=request,context=context))


@csrf_exempt   
def courses_update(request):
    call_command('clearsessions')
   
    if request.method=='POST':
        cid=request.POST.get('courseid')
        course=CoursePrimary.objects.get(courseid=cid)
        form=Courses_Form_Edit(request.POST, request.FILES)
        form.instance=course
      #   form.fields['courseid'].disabled = True
        if form.is_valid():
            form.save()
        print('Course Updated!!')
        return redirect(request=request, to='/courses_home')
    else:
        return redirect(request=request, to='/courses_home')


def courses_add(request):
  call_command('clearsessions')
  course_form=Courses_Form()

  course_form.method='POST'
  return render(request,
                'courses_home.html',
                {'course_form':course_form}
                )
  # template = loader.get_template('courses_add.html')
  # return HttpResponse(template.render())

# ----------------------Course Views---------------------
@csrf_exempt   
def courses_addition(request):
    call_command('clearsessions')
    if request.method=='POST':
      
        form=Courses_Form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
     
        print('Course added successfully!!!')
        # request.session['uname']=request.POST.get('username')
        # uid=request.POST.get('username')
        # return redirect(request=request, to='/Image_Upload?uname=' + uid)
        return redirect(request=request, to='/courses_home')
    
    else:
        return redirect(request=request, to='/courses_home')

@csrf_exempt     
def courses_getid(request):
   call_command('clearsessions')
   if request.method=='GET':
      print(request.GET.get('cid'))

      coursesdata=CoursePrimary.objects.filter()
      context = {
     'coursesdata' : coursesdata,
     }
      template = loader.get_template('courses_home.html')
      return HttpResponse(template.render(request=request,context=context))

      # return redirect(request=request, to='/courses_home')
   else:
      return redirect(request=request, to='/courses_home')
   

@csrf_exempt
def courses_modalshow(request):
  call_command('clearsessions')
  coursesdata=CoursePrimary.objects.filter()
  context = {
     'coursesdata' : coursesdata,
  }
  template = loader.get_template('courses_home.html')
  return HttpResponse(template.render(request=request,context=context))

      
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Web_User(AbstractUser):
    # firstname=models.CharField(max_length=150, null=False, blank=False )
    # lastname=models.CharField(max_length=150, null=False, blank=False)
    username=models.CharField(max_length=150, unique=True,null=False, blank=False)
    password=models.CharField(max_length=100)
    user_type=models.CharField(max_length=50)
    user_contact=models.CharField(max_length=100)
    path = models.ImageField(upload_to='images/',default='images/default.png')
    # profile_picture = models.ImageField(upload_to='images/', blank=True, null=True)
    
    
    # user_isactive=models.DecimalField(max_digits=1,decimal_places=0, default=0)
    # add additional fields in here
  
    
class College_Data(models.Model):
    collegename=models.CharField(max_length=300)
    collegeweburl=models.CharField(max_length=150)
    principalname=models.CharField(max_length=100)
    principalcontact=models.CharField(max_length=12)
    principalemail=models.CharField(max_length=100)
  
#     user_type=models.CharField(max_length=50)
#     user_email=models.EmailField(max_length=100)
#     user_contact=models.CharField(max_length=100)
#     user_isactive=models.DecimalField(max_digits=1,decimal_places=0, default=0)

    # REQUIRED_FIELDS = ('username', 'password',)
class ProfileImage(models.Model):
    # uname= models.CharField(max_length=255,default='unknown')
    # caption = models.CharField(max_length=255)
    user = models.OneToOneField(Web_User, on_delete=models.CASCADE, default=None)
    path = models.ImageField(upload_to='images/',default='images/default.png')
    def __str__(self):  
        return self.user.username
    
class CourseMaster(models.Model):
    courseid=models.CharField(max_length=50, primary_key=True)
    course_name=models.CharField(max_length=300)
    course_intake=models.IntegerField()
    course_level=models.CharField(max_length=50)
    course_core=models.CharField(max_length=50)
    course_length_years=models.IntegerField()
    course_pattern=models.CharField(max_length=100)
    course_medium=models.CharField(max_length=50)
    course_affiliation=models.CharField(max_length=100)
    course_affiliation_fees=models.IntegerField()
    course_affiliation_validfrom=models.DateField()
    course_affiliation_validupto=models.DateField()
    course_syllabi=models.FileField(upload_to='images/',default='images/syllabusnotfound.pdf')
    

class StudentMaster(models.Model):
    erollmentno=models.CharField(max_length=50, primary_key=True)
    student_name=models.CharField(max_length=150)
    gender=models.CharField(max_length=1)
    father_name=models.CharField(max_length=150)
    mother_name=models.CharField(max_length=150)
    date_of_birth=models.DateField(auto_now_add=True)
    date_of_admission=models.DateField(auto_now_add=True)
    aadhar_no=models.CharField(max_length=15)

    last_school_attended=models.CharField(max_length=300)
    mother_tongue=models.CharField(max_length=20)

    contact_no=models.CharField(max_length=15)
    email_id=models.CharField(max_length=150)
    city=models.CharField(max_length=150)
    district=models.CharField(max_length=150)
    state=models.CharField(max_length=150)

    category=models.CharField(max_length=20)
    caste=models.CharField(max_length=40)
    religion=models.CharField(max_length=20)

    shift=models.CharField(max_length=20)
    local_contact=models.CharField(max_length=15)
    local_address=models.CharField(max_length=150)
    permanent_contact=models.CharField(max_length=15)
    permanent_address=models.CharField(max_length=150)
    admission_batch_year=models.CharField(max_length=12)
    admission_mode=models.CharField(max_length=20)
    admission_category=models.CharField(max_length=20)
    admission_seat_type_alloted=models.CharField(max_length=20)

    
    
    






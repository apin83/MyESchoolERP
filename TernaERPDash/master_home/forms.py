from django import forms
from .models import College_Data, Web_User, ProfileImage,StudentMaster, CourseMaster

class CollegeForm(forms.ModelForm):
    body = forms.CharField(required=True)

    class Meta:
        model = College_Data
        exclude = ("user", )
        
USERTYPE_CHOICES =( 
    ("ADMIN", "ADMIN"), 
    ("PRINCIPAL", "PRINCIPAL"), 
    ("HEAD", "HEAD"), 
    ("TEACHING STAFF", "TEACHING STAFF"), 
    ("ACCOUNTANT", "ACCOUNTANT"), 
    ("CLERK", "CLERK"), 
) 

class Web_User_Form(forms.ModelForm):
    class Meta:
        model = Web_User
        # fields = '__all__' 
        fields = ('first_name', 'last_name', 'email' ,'username', 'password','user_type', 'user_contact','path')   
        widgets = {
            'first_name': forms.TextInput(attrs={'class' : 'form-field d-flex align-items-center'}),
            'last_name' : forms.TextInput(attrs={'class' : 'form-field d-flex align-items-center'}),
            'email' : forms.TextInput(attrs={'class' : 'form-field d-flex align-items-center'}),
            'username' : forms.TextInput(attrs={'class' : 'form-field d-flex align-items-center'}),
            'password' : forms.TextInput(attrs={'class' : 'form-field d-flex align-items-center','type':'password'}),
            'user_type' : forms.TextInput(attrs={'class' : 'form-field d-flex align-items-center'}),
            # 'user_type' : forms.ChoiceField(choices = USERTYPE_CHOICES),
            'user_contact' : forms.TextInput(attrs={'class' : 'form-field d-flex align-items-center'}),
            # 'path' : forms.ImageField(),
            # 'password' : forms.CharField(widget=forms.PasswordInput),
            }
        

        
class Web_Login_Form(forms.ModelForm):
    class Meta:
        model=Web_User
        fields= ('username','password' )
        widgets = {
            'username' : forms.TextInput(attrs={'class' : 'form-field d-flex align-items-center'}),
            'password' : forms.TextInput(attrs={'class' : 'form-field d-flex align-items-center','type':'password'}),
            
            # 'submit' : forms.inpu(attrs={'class' : 'btn mt-2','type':'submit'}),
            }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileImage
        # exclude = ("id", )
        fields = '__all__' 
        # fields = ('uname', 'caption', 'image', )   
          
    
class Student_Data_Form(forms.ModelForm):
    class Meta:
        model = StudentMaster
        # exclude = ("id", )
        fields = '__all__' 
        # fields = ('uname', 'caption', 'image', )     
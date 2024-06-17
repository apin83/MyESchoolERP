from django import forms
from .models import CoursePrimary
        
# class Courses_Form(forms.ModelForm):
#     body = forms.CharField(required=True)

#     class Meta:
#         model = CoursePrimary
#         fields = '__all__' 
        

class Courses_Form(forms.ModelForm):
    class Meta:
        model=CoursePrimary
        fields= ('courseid','course_name', 'course_intake','course_level', 'course_core', 'course_length_years', 'course_pattern', 'course_medium', 'course_affiliation','course_affiliation_fees', 'course_affiliation_validfrom', 'course_affiliation_validupto', 'course_syllabi' )
        widgets = {
            'courseid' : forms.TextInput(attrs={'class' : 'fs-5 form-field d-flex text-monospace align-items-center m-2 w-100', 'placeholder':'CourseID'}),
            'course_name' : forms.TextInput(attrs={'class' : 'fs-5 form-field d-flex text-monospace align-items-center m-2 w-100', 'placeholder':'Course Name'}),
            'course_intake' : forms.TextInput(attrs={'class' : 'fs-5 form-field d-flex text-monospace align-items-center m-2  w-100', 'placeholder':'Intake'}),
            'course_level' : forms.TextInput(attrs={'class' : 'fs-5 form-field d-flex text-monospace align-items-center m-2 w-100', 'placeholder':'Level'}),
            'course_core' : forms.TextInput(attrs={'class' : 'fs-5 form-field d-flex text-monospace align-items-center m-2 w-100', 'placeholder':'Core'}),
            'course_length_years' : forms.TextInput(attrs={'class' : 'fs-5 form-field d-flex text-monospace align-items-center m-2 w-100', 'placeholder':'Span in Years/Months'}),
            'course_pattern' : forms.TextInput(attrs={'class' : 'fs-5 form-field d-flex text-monospace align-items-center m-2 w-100', 'placeholder':'Pattern'}),
            'course_medium' : forms.TextInput(attrs={'class' : 'fs-5 form-field d-flex text-monospace align-items-center m-2 w-100', 'placeholder':'Medium'}),
            'course_affiliation' : forms.TextInput(attrs={'class' : 'fs-5 form-field d-flex text-monospace align-items-center m-2 w-100', 'placeholder':'Affiliation'}),
            'course_affiliation_fees' : forms.TextInput(attrs={'class' : 'fs-5 form-field d-flex text-monospace align-items-center m-2 w-100', 'placeholder':'Affiliation Fees'}),
            'course_affiliation_validfrom' : forms.DateInput(attrs={'class' : 'fs-5 form-field d-flex text-monospace align-items-center m-2 w-100', 'placeholder':'Affiliation From'}),
            'course_affiliation_validupto' : forms.DateInput(attrs={'class' : 'fs-5 form-field d-flex text-monospace align-items-center m-2 w-100', 'placeholder':'Affiliation UpTo'}),
            'course_syllabi' : forms.FileInput(attrs={'class' : 'fs-5 form-control form-control-sm m-2 w-100 text-monospace', 'placeholder':'Syllabus'}),

            # 'btnSave' : forms.boundfield(attrs={'class' : 'bg-primary', 'type' : 'submit'}),
            # 'submit' : forms.inpu(attrs={'class' : 'btn mt-2','type':'submit'}),
            }

class Courses_Form_Edit(forms.ModelForm):
    class Meta:
        model=CoursePrimary
        fields= ('courseid','course_name', 'course_intake','course_level', 'course_core', 'course_length_years', 'course_pattern', 'course_medium', 'course_affiliation','course_affiliation_fees', 'course_affiliation_validfrom', 'course_affiliation_validupto', 'course_syllabi' )
        widgets = {
            'courseid' : forms.TextInput(attrs={'class' : 'fs-5 form-field d-flex text-monospace align-items-center m-2 w-100', 'placeholder':'CourseID'}),
            'course_name' : forms.TextInput(attrs={'class' : 'fs-5 form-field d-flex text-monospace align-items-center m-2 w-100', 'placeholder':'Course Name'}),
            'course_intake' : forms.TextInput(attrs={'class' : 'fs-5 form-field d-flex text-monospace align-items-center m-2  w-100', 'placeholder':'Intake'}),
            'course_level' : forms.TextInput(attrs={'class' : 'fs-5 form-field d-flex text-monospace align-items-center m-2 w-100', 'placeholder':'Level'}),
            'course_core' : forms.TextInput(attrs={'class' : 'fs-5 form-field d-flex text-monospace align-items-center m-2 w-100', 'placeholder':'Core'}),
            'course_length_years' : forms.TextInput(attrs={'class' : 'fs-5 form-field d-flex text-monospace align-items-center m-2 w-100', 'placeholder':'Span in Years/Months'}),
            'course_pattern' : forms.TextInput(attrs={'class' : 'fs-5 form-field d-flex text-monospace align-items-center m-2 w-100', 'placeholder':'Pattern'}),
            'course_medium' : forms.TextInput(attrs={'class' : 'fs-5 form-field d-flex text-monospace align-items-center m-2 w-100', 'placeholder':'Medium'}),
            'course_affiliation' : forms.TextInput(attrs={'class' : 'fs-5 form-field d-flex text-monospace align-items-center m-2 w-100', 'placeholder':'Affiliation'}),
            'course_affiliation_fees' : forms.TextInput(attrs={'class' : 'fs-5 form-field d-flex text-monospace align-items-center m-2 w-100', 'placeholder':'Affiliation Fees'}),
            'course_affiliation_validfrom' : forms.DateInput(attrs={'class' : 'fs-5 form-field d-flex text-monospace align-items-center m-2 w-100', 'placeholder':'Affiliation From'}),
            'course_affiliation_validupto' : forms.DateInput(attrs={'class' : 'fs-5 form-field d-flex text-monospace align-items-center m-2 w-100', 'placeholder':'Affiliation UpTo'}),
            'course_syllabi' : forms.FileInput(attrs={'class' : 'fs-5 form-control form-control-sm m-2 w-100 text-monospace', 'placeholder':'Syllabus'}),

            # 'btnSave' : forms.boundfield(attrs={'class' : 'bg-primary', 'type' : 'submit'}),
            # 'submit' : forms.inpu(attrs={'class' : 'btn mt-2','type':'submit'}),
            }
    def __init__(self, *args, **kwargs):
        super(Courses_Form_Edit, self).__init__(*args, **kwargs)
        self.fields['courseid'].disabled = True
        # self.fields['email'].disabled = True
from django.db import models

# Create your models here.
class CoursePrimary(models.Model):
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
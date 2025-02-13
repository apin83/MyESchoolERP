# Generated by Django 4.2.9 on 2024-03-28 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master_home', '0023_alter_coursemaster_course_affiliation_validfrom_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursemaster',
            name='course_length_years',
            field=models.IntegerField(default=4),
        ),
        migrations.AddField(
            model_name='coursemaster',
            name='course_medium',
            field=models.CharField(default='English', max_length=50),
        ),
        migrations.AddField(
            model_name='coursemaster',
            name='course_pattern',
            field=models.CharField(default='Semester', max_length=100),
        ),
    ]

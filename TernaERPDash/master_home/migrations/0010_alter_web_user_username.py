# Generated by Django 4.2.9 on 2024-02-29 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master_home', '0009_student_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='web_user',
            name='username',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]

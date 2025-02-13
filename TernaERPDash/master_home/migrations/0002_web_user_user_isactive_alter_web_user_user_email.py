# Generated by Django 4.2.9 on 2024-01-31 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master_home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='web_user',
            name='user_isactive',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=1),
        ),
        migrations.AlterField(
            model_name='web_user',
            name='user_email',
            field=models.EmailField(max_length=100),
        ),
    ]

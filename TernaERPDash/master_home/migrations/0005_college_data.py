# Generated by Django 4.2.9 on 2024-02-02 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master_home', '0004_alter_web_user_options_alter_web_user_managers_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='College_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collegename', models.CharField(max_length=300)),
                ('collegeweburl', models.CharField(max_length=150)),
                ('principalname', models.CharField(max_length=100)),
                ('principalcontact', models.CharField(max_length=12)),
                ('principalemail', models.CharField(max_length=100)),
            ],
        ),
    ]

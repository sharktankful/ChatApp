# Generated by Django 4.1.2 on 2023-01-09 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_profile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='static/chat/images/default-profile-photo.jpg', null=True, upload_to='images/profile/'),
        ),
    ]
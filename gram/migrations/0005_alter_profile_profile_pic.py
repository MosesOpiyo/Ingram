# Generated by Django 3.2.8 on 2021-10-19 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gram', '0004_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='pw4.jpg', upload_to='profile/'),
        ),
    ]
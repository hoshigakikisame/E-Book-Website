# Generated by Django 3.1.4 on 2020-12-04 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_photo',
            field=models.ImageField(blank=True, default='index.png', upload_to=''),
        ),
    ]
# Generated by Django 3.1.4 on 2020-12-01 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebook', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ebook',
            name='thumbnail',
            field=models.ImageField(default='/static/img/default-img.png', upload_to='documents/'),
        ),
    ]

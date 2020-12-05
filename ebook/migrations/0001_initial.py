# Generated by Django 3.1.4 on 2020-12-01 17:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ebook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(blank=True, max_length=255)),
                ('file', models.FileField(upload_to='documents/')),
                ('upload', models.DateTimeField(auto_now_add=True)),
                ('pengarang', models.CharField(blank=True, max_length=255)),
                ('penerbit', models.CharField(blank=True, max_length=255)),
                ('slug', models.SlugField(blank=True, editable=False)),
                ('author', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

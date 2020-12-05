from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user',null=True, blank=True)
	profile_photo = models.ImageField(blank=True, default='/index.png')

	def save(self, *args, **kwargs):
		super(UserProfile, self).save(*args, **kwargs)
		super().save()

	def __str__(self):
		return "{}'s - Profile".format(self.user)
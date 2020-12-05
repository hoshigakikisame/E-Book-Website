from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.
class Ebook(models.Model):
	judul = models.CharField(max_length=255, blank=True)
	thumbnail = models.ImageField(upload_to='documents/', default="/default-img.png")
	author = models.ForeignKey(User, on_delete=models.CASCADE, default=1, blank=True, null=True)
	file = models.FileField(upload_to='documents/')
	upload = models.DateTimeField(auto_now_add=True)
	pengarang = models.CharField(max_length=255, blank=True)
	penerbit = models.CharField(max_length=255, blank=True)
	deskripsi = models.TextField(default="Beautiful masterpiece")
	slug = models.SlugField(blank=True, editable=False)

	def save(self, *args, **kwargs):
		super(Ebook, self).save(*args, **kwargs)
		self.slug = slugify(str(self.id) + self.judul)
		super().save()

	def __str__(self):
		return '{} | {}'.format(self.author, self.judul)
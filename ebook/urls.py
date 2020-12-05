from django.urls import path 
from . import views

urlpatterns = [
	path('upload/', views.upload_ebook, name="upload"),
	path('', views.ebook, name="ebook_index"),
]
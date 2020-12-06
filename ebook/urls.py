from django.urls import path 
from . import views

urlpatterns = [
	path('upload/', views.upload_ebook, name="upload"),
	path('delete/<int:ebook_id>', views.deleteEbook, name="deleteEbook"),
	path('', views.ebook, name="ebook_index"),
	path('update/<int:ebook_id>', views.updateEbook, name="updateEbook"),

]
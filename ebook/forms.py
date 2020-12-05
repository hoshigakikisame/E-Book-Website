from django import forms
from ebook.models import Ebook

class EbookForm(forms.ModelForm):
	class Meta:
		model = Ebook
		fields = ['judul', 'thumbnail', 'file', 'pengarang', 'penerbit', 'deskripsi']
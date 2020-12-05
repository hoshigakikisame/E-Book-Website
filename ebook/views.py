from django.shortcuts import render, redirect
from .models import Ebook
from .forms import EbookForm

# Create your views here.
def ebook(request):
	all_ebook = Ebook.objects.all().order_by('-upload')
	context = {
		'all_ebook':all_ebook,
	}
	return render(request, 'ebook/ebook.html', context)

def upload_ebook(request):
	form = EbookForm(request.POST or None, request.FILES or None)
	context = {
		'form':form,
	}
	if request.method == 'POST':
		if form.is_valid():
			newpost = form.save(commit=False)
			newpost.author = request.user
			newpost.save()
			return redirect('auth:profile')

		else:
			print("not valid")
			print(form.errors)

	return render(request, 'ebook/upload.html', context)
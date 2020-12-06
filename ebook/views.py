from django.shortcuts import render, redirect
from .models import Ebook
from .forms import EbookForm
from django.contrib.auth.decorators import login_required


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

@login_required(login_url="/auth/signin/")
def updateEbook(request, ebook_id):
	update_ebook = Ebook.objects.get(id=ebook_id)

	data = {
		'judul' : update_ebook.judul,
		'thumbnail':update_ebook.thumbnail,
		'file'	: update_ebook.file,
		'pengarang' : update_ebook.pengarang,
		'penerbit' : update_ebook.penerbit,
		'deskripsi' : update_ebook.deskripsi,
	}

	update_ebook_form = EbookForm(request.POST or None, request.FILES or None, initial=data, instance=update_ebook)

	if request.method == 'POST':
		if update_ebook_form.is_valid():
			update_ebook_form.save()
		return redirect('auth:profile')

	context = {
		'update_ebook_form' : update_ebook_form,
	}
	print()
	return render(request, 'ebook/update.html', context)


@login_required(login_url="/auth/signin/")
def deleteEbook(request, ebook_id):
	delete_ebook = Ebook.objects.get(id=ebook_id)
	delete_ebook.delete() 

	return redirect('user:profile')
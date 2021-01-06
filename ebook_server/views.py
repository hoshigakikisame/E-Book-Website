from django.shortcuts import render
from ebook.models import Ebook

def index(request):
	ebook = Ebook.objects.all().order_by('-upload')[:6]
	return render(request, 'index.html', {'ebook_preview':ebook})

def search(request):

	if 'query' in request.GET:
		query = request.GET['query']
		query = query.strip()
		ebook_search = Ebook.objects.filter(judul__icontains=query).order_by('-upload')
	
		context = {
			'q':query,
			'ebook_search':ebook_search,
		}

		return render(request, 'search.html', context)

	return redirect(index)
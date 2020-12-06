from django.shortcuts import render
from ebook.models import Ebook

def index(request):
	return render(request, 'index.html')

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
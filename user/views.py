from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import logout
from user.models import UserProfile
from ebook.models import Ebook

# Create your views here.
def signin_view(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('index')
		else:
			print('gaiso login')
			return render(request, "user/signin.html", {'message':'Cannot login'})
	return render(request, "user/signin.html")

def signup_view(request):
	if request.method == "POST":
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		user = User.objects.create_user(username, email, password)
		UserProfile.objects.create(user=User.objects.get(username=username))
		if user:
			return redirect('auth:signin')
	return render(request, 'user/signup.html')

def profile(request):
	user = UserProfile.objects.get(user=request.user)
	ebook_user = Ebook.objects.filter(author=user.user).order_by('-upload')

	context = {
		'user':user,
		'photo':user.profile_photo.url,
		'ebooks':ebook_user,
	}
	return render(request, 'user/profile.html', context)


def logout_view(request):
    logout(request)
    return redirect('index')
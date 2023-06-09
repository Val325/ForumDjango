from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse 
from django.http import JsonResponse
from .. import forms
from .. import models
from django.core.paginator import Paginator
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger

def profile(request):
	session = request.session['auth']
	user = request.session['username']
	UserData = models.UserProfile.objects.all()
	print("userdata:", UserData)
	
	profile_img = get_object_or_404(UserData, user=user)
	print('user', profile_img.avatar)
	img = profile_img.avatar
	if request.method == 'GET':
		form = forms.UserProfileForm()
		return render(request, 'profile.html', { 
											"session": session,
											"user": user,
											"form": form,
											"img":profile_img.avatar

										})
	else:
		if request.method == "POST" and session:  
			form = forms.UserProfileForm(request.POST, request.FILES)
			print("form:", form)
			if form.is_valid():
				img = form.instance
				post = form.save(commit=False)
				post.user_id = user # change is here
				post.save()
			return render(request, 'profile.html', { 
											"session": session,
											"user": user,
											"form": form,
											"img":img
										})

	
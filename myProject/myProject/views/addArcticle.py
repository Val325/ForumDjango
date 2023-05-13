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

def add_article(request):
	session = request.session['auth']
	user = request.session['username']
	if request.method == 'GET':
		form = forms.UserForm()
		return render(request, 'addArticle.html', { 
											"session": session,
											"user": user,
											"form": form,
										})

	else:
		if request.method == "POST" and session:  
			form = forms.UserForm(request.POST, request.FILES)


			if form.is_valid():
				img = form.instance
				post = form.save(commit=False)
				post.category = request.POST.get('category')
				post.user_id = user
				post.save()
			
			return render(request, 'addArticle.html', { 
											"session": session,
											"user": user,
											"form": form,
										})

	
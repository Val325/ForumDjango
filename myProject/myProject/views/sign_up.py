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

def sign_up(request):
    if request.method == 'GET':
        form = forms.RegisterForm()
        return render(request, 'registration.html', { 'form': form})
    else:
    	print(request.POST)
    	form = forms.RegisterForm(request.POST)
    	if form.is_valid():
    		user = form.save(commit=False)
    		user.save()
    		return redirect("/login/")
    	return redirect("/reg/")
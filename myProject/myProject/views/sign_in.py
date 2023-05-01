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

def sign_in(request):
    if request.method == 'GET':
        form = forms.LoginForm()
        return render(request, 'login.html', {'form': form})
    else:
    	form = forms.LoginForm(request.POST)

    	if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)

            if user:
                login(request, user)
                messages.success(request,f'Hi {username.title()}, welcome back!')
                request.session['auth'] = True 
                request.session['username'] = username.title()
                return redirect('/')

    #messages.error(request,f'Invalid username or password')
    return render(request,'login.html',{'form': form})
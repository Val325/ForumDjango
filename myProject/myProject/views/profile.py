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
	return render(request, 'profile.html', { 
											"session": session,
											"user": user
										})
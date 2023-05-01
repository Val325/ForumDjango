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

def Posts(request, id):
	DataText = models.textData.objects.all()
	post = get_object_or_404(DataText, id=id)
	subposts = post.subpost.all()
	session = False

	try:
		session = request.session['auth']
		print("auth:")
		print("------------")
		print(request.session['auth'])
		print("username:")
		print(request.session['username'])
		print("------------")
	except KeyError:
		print('Is not auth!')

	print("------------")
	print("   Subpost  ")
	print("------------")
	print(subposts)
	print("------------")
	indexChoiceArray = int(id) - 1
	print('indexChoiceArray',indexChoiceArray)
	#
	DataId = [] 
	DataName = []
	DataTex = [] 
	DataImage = []

	print("------------")
	for data in DataText:
		print(f"{data.id}.{data.user} - {data.textdata} - {data.image}")
		DataId.append(data.id)
		DataName.append(data.user)
		DataTex.append(data.textdata) 
		DataImage.append(data.image)


	post = {
		"id": DataId[indexChoiceArray], 
		"name": DataName[indexChoiceArray],
		"text": DataTex[indexChoiceArray],
		"image": DataImage[indexChoiceArray]
	}

	if request.method == "POST":
		post_form = forms.SubPostForm(request.POST or None, request.FILES or None, use_required_attribute=False)
		
		if post_form.is_valid():

            # Create Comment object but don't save to database yet
			subpost = post_form.save(commit=False)

			subpost.user = request.user

            # Assign the current post to the comment
			subpost.post = models.textData.objects.get(id=id)
            # Save the comment to the database
			subpost.save()

	form = forms.UserForm(request.POST, request.FILES)
	

	return render(request, 'subposts.html', {'form': form, 'post': post, 'idform': DataId[indexChoiceArray], 'subposts': subposts, "session": session})
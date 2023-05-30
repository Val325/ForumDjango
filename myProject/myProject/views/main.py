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
from django.db.models import Max
def MainText(request):
    DataText = models.textData.objects.all()
    print("----------")
    print("Query to DB", DataText.query)
    print("----------")
    img = None 
    page_num = request.GET.get('page', 1)
    paginator = Paginator(DataText, 6)
    session = False
    user = ""
    print("----------")
    print("max post")
    print(DataText.aggregate(Max("id")))
    print("----------")

    print("----------")
    print(request.POST)
    print("----------")
    for data in DataText:
    	print(f"{data.id}.{data.user} - {data.textdata} - {data.image}")


    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    try:
        session = request.session['auth']
        user = request.session['username']

        textdata = request.POST.get('textdata')
        image = request.FILES.get('image')

        # Призначити значення для user_id
        user_id = user



        print('Sucsessful')
        print(session)

        if request.method == "POST" and session:  
            form = forms.UserForm(request.POST, request.FILES)


            if form.is_valid():
                img = form.instance
                post = form.save(commit=False)
                post.category = request.POST.get('category')
                post.user_id = user
                post.save()

                return render(request, 'main.html', {'form': form,
												 'DataText': DataText,
												 "img": img, 
												 'page_obj': page_obj, 
												 "session": session,
												 "user": user}) 

    except KeyError:
        print('Is not auth!')

	

    print(DataText)
	
	
    form = forms.UserForm()
    return render(request, 'main.html', {'form': form, 'DataText': DataText, "img": img, 'page_obj': page_obj, "session": session})

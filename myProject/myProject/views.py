from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse 
from django.http import JsonResponse
from .forms import UserForm
from .forms import LoginForm, RegisterForm, SubPostForm
from .models import textData
from django.core.paginator import Paginator
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger






def MainText(request):
	DataText = textData.objects.all()
	img = None 
	page_num = request.GET.get('page', 1)
	paginator = Paginator(DataText, 6)
	session = False
	user = ""

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
			form = UserForm(request.POST, request.FILES)


			if form.is_valid():
				img = form.instance
				post = form.save(commit=False)
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
	
	
	
	form = UserForm()
	return render(request, 'main.html', {'form': form, 'DataText': DataText, "img": img, 'page_obj': page_obj, "session": session})

def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'registration.html', { 'form': form})
    else:
    	print(request.POST)
    	form = RegisterForm(request.POST)
    	if form.is_valid():
    		user = form.save(commit=False)
    		user.save()
    		return HttpResponse('<h1>Успешно!</h1>')
    	return HttpResponse('<h1>Не успешно!</h1>')

    
def sign_in(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    else:
    	form = LoginForm(request.POST)

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

@login_required
def logoutUser(request):
    

    print("Logged out successfully!")
    logout(request)
    return HttpResponse('<h1>logout</h1>')

def About(request):
	return HttpResponse('<h1>About us</h1>')

def Posts(request, id):
	DataText = textData.objects.all()
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

	print("------------")
	print(DataId[indexChoiceArray]) 
	print(DataName[indexChoiceArray])
	print(DataTex[indexChoiceArray]) 
	print(DataImage[indexChoiceArray])
	print("------------")

	post = {
		"id": DataId[indexChoiceArray], 
		"name": DataName[indexChoiceArray],
		"text": DataTex[indexChoiceArray],
		"image": DataImage[indexChoiceArray]
	}

	if request.method == "POST":
		post_form = SubPostForm(request.POST or None, request.FILES or None, use_required_attribute=False)
		
		if post_form.is_valid():

            # Create Comment object but don't save to database yet
			subpost = post_form.save(commit=False)

			subpost.user = request.user

            # Assign the current post to the comment
			subpost.post = textData.objects.get(id=id)
            # Save the comment to the database
			subpost.save()

	form = UserForm(request.POST, request.FILES)
	

	return render(request, 'subposts.html', {'form': form, 'post': post, 'idform': DataId[indexChoiceArray], 'subposts': subposts, "session": session})

def FakeAPI(request):
	return JsonResponse({"Dick": "Vagina", "Size dick": 38})


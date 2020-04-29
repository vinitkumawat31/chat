from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import ChatMessage
import json 

def index(request):
    return render(request, 'chat/index.html',{})


def login_request(request):
	if request.method == 'POST':
		form = AuthenticationForm(request, request.POST)
		if form.is_valid():
			username = form.cleaned_data.get("username")
			password = form.cleaned_data.get("password")
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request,user)
				messages.info(request,"you are logged in as : "+str(username))
				User = user
				return redirect("chat:index")
			else:
				messages.error(request, "username or password invaid!")
		else:
				messages.error(request, "username or password invaid!")
	form = AuthenticationForm()
	return render(request,"chat/login.html",context={"form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "logged out successfully!")
	return redirect("chat:index")

def room(request, room_name):
	current_user = request.user
	msg_data = None
	if current_user is not None:
		msg_data = ChatMessage.objects.filter(room=room_name)
		msg_data = msg_data.all()

	return render(request, 'chat/room.html', context={'room_name': room_name ,'msg_data':msg_data})
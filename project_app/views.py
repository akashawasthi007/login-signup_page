from django.shortcuts import render
from project_app.forms import UserForm,fform
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User
#from project_app.models import Usr
# Create your views here.

def password_reset(request):
	form=fform()
	if form.is_valid():
		print("pass")
	else:
		print("fail")
	return render(request,"sign_in/password_reset.html",{'form':form})

def logn(request):
	form=AuthenticationForm()
	if request.method == "POST":
		form=AuthenticationForm(request,data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return render(request,'sign_in/success.html')
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
		#return render(request,'sign_in/success.html')
	return render(request,"sign_in/login.html",context={'form':form})

def lgout(request):
	logout(request)
	return render(request,"sign_in/login.html")

def register(request):
    form=UserForm()
    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.refresh_from_db()
#            user.Usr.user=form.cleaned_data.get('user')
#            user.Usr.name=form.cleaned_data.get('name')
#            user.Usr.email=form.cleaned_data.get('email')
#            user.Usr.gender=form.cleaned_data.get('gender')
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            print("username :"+form.cleaned_data['username'])
            user=authenticate(username=username,password=password)
            login(request,user)
            return render(request,'sign_in/login.html',{'form':form})
    return render(request,'sign_in/register.html',{'form':form})

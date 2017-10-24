# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .forms import UserRegistrationForm
from .models import Listing
# Create your views here.

def home(request):
	return render(request,'insta/home.html',{'home':home})


def signupp(request,backend='django.contrib.auth.backends.ModelBackend'):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			user = Listing()
			obj = form.cleaned_data;
			
			user.username = obj['username']
			user.password = obj['password']
			user.email = obj['email']
			user1 = authenticate(username=user.username, email=user.email)
			user.save()
			#if user is not None:
			login(request, user1,backend='django.contrib.auth.backends.ModelBackend')
			return HttpResponseRedirect('home') 
	else:				
		form = UserRegistrationForm()
	return render(request,'insta/index.html',{'form':form})	
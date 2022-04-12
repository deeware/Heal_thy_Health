from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime,date

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import *
from .forms import *



@csrf_exempt
def index(request,choice = None):
    try:
        obj = Person.objects.get(user = request.user)
        return redirect('recommended')
    except:
        
        category = Category.objects.all()
        videos = Video.objects.all()
        
        choice = request.POST.get('category')
        
        if choice and choice!="All":
            videos = Video.objects.filter(category = choice)
        
        return render(request,'index.html',
                    context = {'category' : category,
                                'videos' : videos })
    
@csrf_exempt
def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        frm = CreateUserForm()

        if request.method == "POST":
            frm = CreateUserForm(request.POST)
            if frm.is_valid():
                frm.save()
                return redirect('login')
        return render(request,'register.html',{'form':frm})
    
    
@csrf_exempt
def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == "POST":
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request,username=username, password=password)

			if user:
				login(request,user)
				return redirect('home')
			else:
				return render(request,'login.html')

		return render(request, 'login.html')



@login_required(login_url='login')
def logoutUser(request):
	logout(request)
	return redirect('home')

@csrf_exempt
@login_required(login_url='login')
def createProfile(request):
    try:
        obj = Person.objects.get(user = request.user)
        return redirect('update')
    except:
        
        frm = ProfileForm(request.POST or None)
        
        if request.method == "POST" and frm.is_valid():
            a = request.user
            b = frm.cleaned_data.get("name")
            c = frm.cleaned_data.get("dob")
            d = frm.cleaned_data.get("gender")
            e = frm.cleaned_data.get("height")
            f = frm.cleaned_data.get("weight")
            g = frm.cleaned_data.get("preferences")
            obj = Person(user = a, 
                        name = b,
                        dob = c,
                        gender = d,
                        height = e,
                        weight = f)
            obj.save()
            obj.preferences.add(*g)
            obj.save()
            
            
            return redirect("profile")

        context = {"form":frm}
        return render(request,'createprofile.html', context)

@csrf_exempt
@login_required(login_url='login')
def updateProfile(request):
    try:
        
        obj = Person.objects.get(user = request.user)
        frm = ProfileForm(request.POST or None,instance = obj)
        
        if request.method == "POST" and frm.is_valid():
            obj.name = frm.cleaned_data.get("name")
            obj.dob = frm.cleaned_data.get("dob")
            obj.gender = frm.cleaned_data.get("gender")
            obj.height = frm.cleaned_data.get("height")
            obj.weight = frm.cleaned_data.get("weight")
            obj.preferences.clear()
            obj.preferences.add(*frm.cleaned_data.get("preferences"))
            
            obj.save()
            print(type(obj.preferences))
            return redirect("profile")
        context = {"form":frm}
        return render(request,'createprofile.html',context)  
    except:
        return redirect('create')  
              
@csrf_exempt
@login_required(login_url='login')
def recommended(request):
    try:
        obj = Person.objects.get(user = request.user)
        videos = Video.objects.filter(category__in = obj.preferences.all()).distinct()
        category = Category.objects.all()
        
        choice = request.POST.get('category')
        
        if choice=="All":
            videos = Video.objects.all()
        elif choice:
            videos = Video.objects.filter(category = choice)
        
        
        return render(request,'index.html',
                    context = {'category' : category,
                                'videos' : videos })
    except:
        return redirect('home')
        
        
@csrf_exempt
@login_required(login_url='login')
def profile(request):
    try :
        obj = Person.objects.get(user = request.user)
        return render(request, 'profile.html', context = {'Person':obj})
    except Exception as e:
        print(e)
        return redirect('create')



        
    

from django import forms
from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import * 

# Both these Classes will allow capturing date & time in HTML5 way

class CreateUserForm(UserCreationForm):

	password1 = forms.CharField(label="Password",
		widget=forms.PasswordInput(attrs={'placeholder':"Password",'class':"bg-gray-200 rounded w-full text-gray-700 focus:outline-none border-b-4 border-gray-300 focus:border-purple-600 transition duration-500 px-3 pb-3"}))
	password2 = forms.CharField(label="Confirm Password",
		widget=forms.PasswordInput(attrs={'placeholder':"Password",'class':"bg-gray-200 rounded w-full text-gray-700 focus:outline-none border-b-4 border-gray-300 focus:border-purple-600 transition duration-500 px-3 pb-3"}))
    
	class Meta:
		model = User
		fields = ['username','email']
		widgets = {
            'username': forms.TextInput(attrs={'placeholder':"deeware",'class':"bg-gray-200 rounded w-full text-gray-700 focus:outline-none border-b-4 border-gray-300 focus:border-purple-600 transition duration-500 px-3 pb-3"}),
            'email': forms.TextInput(attrs={'placeholder':"your@email.com",'class':"bg-gray-200 rounded w-full text-gray-700 focus:outline-none border-b-4 border-gray-300 focus:border-purple-600 transition duration-500 px-3 pb-3"}),
        }

class DateInput(forms.DateInput):
	input_type='date'


class ProfileForm(forms.ModelForm):
	preferences = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
	dob = forms.DateField(widget=DateInput(attrs={'class':"bg-gray-200 rounded w-full text-gray-700 focus:outline-none border-b-4 border-gray-300 focus:border-purple-600 transition duration-500 px-3 pb-3"}))
	class Meta:
		model=Person
		fields = ['name','dob','gender','height','weight','preferences']
		widgets = {
            'name': forms.TextInput(attrs={'placeholder':"Sam Miller",'class':"bg-gray-200 rounded w-full text-gray-700 focus:outline-none border-b-4 border-gray-300 focus:border-purple-600 transition duration-500 px-3 pb-3"}),
            'gender': forms.Select(attrs={'class':"bg-gray-200 rounded w-full text-gray-700 focus:outline-none border-b-4 border-gray-300 focus:border-purple-600 transition duration-500 px-3 pb-3"}),
            'height': forms.NumberInput(attrs={'placeholder':"175 (cm)",'class':"bg-gray-200 rounded w-full text-gray-700 focus:outline-none border-b-4 border-gray-300 focus:border-purple-600 transition duration-500 px-3 pb-3"}),
            'weight': forms.NumberInput(attrs={'placeholder':"65 (kg)",'class':"bg-gray-200 rounded w-full text-gray-700 focus:outline-none border-b-4 border-gray-300 focus:border-purple-600 transition duration-500 px-3 pb-3"}),
        }
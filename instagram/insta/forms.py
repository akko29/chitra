from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.Form):
	username = forms.CharField(required=True,label="Username",max_length=50)
	first = forms.CharField(required=True,label="First Name",max_length=150)
	last = forms.CharField(required=False,label = "Last Name", max_length = 150)
	password = forms.CharField(required=True, label="password", max_length=50, widget = forms.PasswordInput())
	email = forms.EmailField(required=True, label="Email",max_length=50)

	# def save(self):
	# 	data = self.cleaned_data
	# 	user = User.object.create(username=data['username'],first_name = data['first'],last_name = data['last'],email= data['email'],pass = data['password'])
	# 	user.save()
	from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
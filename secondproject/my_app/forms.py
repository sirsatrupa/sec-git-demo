from django import forms
from .models import Batch, Feedback, Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class student(forms.Form):
    roll_no = forms.IntegerField(label="Enter your roll number")
    name = forms.CharField(label="Ener your name", max_length=30)
    email = forms.EmailField(label="Enter your email")

class BatchForm(forms.ModelForm):
    class Meta:
        model = Batch 
        fields = ('batch_no', 'module_name' ,'time' ,'lab_no')

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','first_name','email','password1','password2')


class SignupForm(UserCreationForm):

    class Meta:
        model=User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']


class FeedbackEntry(forms.ModelForm):
    class Meta:
        model=Feedback
        fields = ['username','feedback']


class ContactEntry(forms.ModelForm):
    class Meta:
        model = Contact
        fields=('name','email','contact','course','help')
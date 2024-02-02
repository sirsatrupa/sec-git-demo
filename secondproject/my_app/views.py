from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm   # for signin view
from django.contrib.auth import authenticate, login, logout # for sign in
from django.http import HttpResponse
from django.contrib import messages
from .forms import SignupForm, BatchForm


# Create your views here.
# def index(request):
#     s = student() # create student class object
#     return render(request, 'index.html', {'student_record':s})

def home(request):
    return render(request, 'home.html')


def createbatch(request):
    if request.method == 'POST':
        cb = BatchForm(request.POST)
        if cb.is_valid():
            cb.save()
        #return redirect(reversed('show'))
        return redirect('show')# we put direct url because for redirect(reversed) it was showing error: object reversed error
    else:
        cb = BatchForm()
    return render(request, 'createbatch.html',{'BatchForm':cb})


from .models import Batch
def showbatch(request): 
    show_batch = Batch.objects.all()
    return render(request, 'showbatch.html',{'show_data': show_batch})

# simple sign up view
# def signup(request):
#     fm = SignupForm()
#     return render(request, 'register.html', {'reg_fm': fm})

# sign up: post methos to the database
# def signup(request):
#     if request.method == 'POST':
#         fm = SignupForm(request.POST)
#         if fm.is_valid():
#             fm.save()
#         return redirect('/signin')
#     else:
#         fm = SignupForm()
#     return render(request, 'register.html', {'signup_form': fm})

def signup(request):
    if request.method == "POST":
        fm = SignupForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'You have register successfully.')
            return redirect("/signin")
    else:
        fm = SignupForm()
    return render(request, "register.html", {'reg_fm':fm})

def signin(request):
    if request.method == "POST":
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            #feed = FeedbackEntry()
            if user is not None:
                login(request, user)
                return render(request, 'signin.html', {'user': user, })
                # return redirect("/feedback")
    else:
        fm = AuthenticationForm()
    return render(request, "signin.html", {'user_data': fm})

# Sign out: log out is a built in function
def signout(request):
    logout(request)
    return redirect("/signin")


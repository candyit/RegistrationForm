from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# from forms import Userform
from loginapp.forms import RegistrationForm
from django.contrib import messages

# Create your views here.

def user_login(request):
    if not request.user.is_authenticated:
        context = {}
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                print(user)
                return HttpResponseRedirect(reverse("user_index"))
            else:
                context = {'error':'please provider valid credentials.'}
                return render(request,"login.html",context)
        else:
            return render(request,"login.html",context)
    else:
        return HttpResponseRedirect(reverse("user_index"))

def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return HttpResponseRedirect(reverse("user_login"))

# @login_required
def user_Index(request):
    if request.user.is_authenticated:
        context = {}
        userDetails = User.objects.all() 
        context['user'] = request.user
        context['userDetails'] = userDetails
        return render(request,"index.html",context)
    else:
        return render(request,"login.html")

def user_registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # username = form.cleaned_date['username']
            # first_name = form.cleaned_date['first_name']
            # last_name = form.cleaned_date['last_name']
            # email = form.cleaned_date['email']
            # password = form.cleaned_date['password']
            # User.objects.create_user(username = 'username',first_name='first_name',last_name='last_name',
            # email='email',password='password')
            messages.success(request,'Account Created Successfully !!')
            form.save()
            # return HttpResponseRedirect(reverse("user_login"))
    else:
        form = RegistrationForm()
    return render(request,"registration.html",{'context':form})

def user_delete(request,myid):
    print(myid)
    print(type(myid))
    user = User.objects.get(id=myid)
    print(user)
    if user.is_valid():
        user.delete()
        return HttpResponseRedirect(reverse("user_index"))


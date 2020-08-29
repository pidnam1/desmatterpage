from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, render
from blog.forms import CompanySignUpForm, ManufacturerSignUpForm
from blog.models import Profile
from django.contrib.auth.models import User
from django import template
from django.contrib.auth.decorators import login_required
from .models import User


def index(request):
    if request.user.is_authenticated  :
        return redirect('/blog/detail/')
    else:
        return render(request, 'blog/home.html')
def signup(request):
    if request.user.is_authenticated  :
        return redirect('/blog/detail/')
    else:
        return render(request, 'blog/signupchoice.html')

def company_signup(request):
    if request.method == 'POST':
        form = CompanySignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            user.refresh_from_db()
            user.profile.is_company = True
            user.profile.business_name = form.cleaned_data.get('business_name')
            user.profile.bio = form.cleaned_data.get('bio')
            user.profile.location = form.cleaned_data.get('location')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/blog/detail/')
    else:
        form = CompanySignUpForm()
    return render(request, 'blog/Companysignup.html', {'form': form})
def manufacturer_signup(request):
    if request.method == 'POST':
        form = ManufacturerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()

            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.is_manufacturer = True
            user.profile.business_name = form.cleaned_data.get('business_name')
            user.profile.bio = form.cleaned_data.get('bio')
            user.profile.location = form.cleaned_data.get('location')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/blog/detail/')
    else:
        form = ManufacturerSignUpForm()
    return render(request, 'blog/ManufacturerSignup.html', {'form': form})

@login_required
def detail(request):
    loggedProfile = Profile.objects.get(user = request.user)

    return render(request, 'blog/LoggedInHome.html', {"profile" : loggedProfile})
@login_required
def myProfile(request):
    loggedProfile = Profile.objects.get(user=request.user)

    return render(request, 'blog/MyProfile.html', {"profile": loggedProfile})
@login_required
def projects(request):
    loggedProfile = Profile.objects.get(user=request.user)

    return render(request, 'blog/Projects.html', {"profile": loggedProfile})
@login_required
def orders(request):
    loggedProfile = Profile.objects.get(user=request.user)

    return render(request, 'blog/Orders.html', {"profile": loggedProfile})
@login_required
def payments(request):
    loggedProfile = Profile.objects.get(user=request.user)

    return render(request, 'blog/Payments.html', {"profile": loggedProfile})
@login_required
def products(request):
    loggedProfile = Profile.objects.get(user=request.user)

    return render(request, 'blog/Products.html', {"profile": loggedProfile})



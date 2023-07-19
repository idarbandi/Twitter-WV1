from django.shortcuts import render, redirect
from .models import Profile, Tweet
from django.contrib import messages
from .forms import TweetForm, SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django import forms


def home(request):
    if request.user.is_authenticated:
        form = TweetForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                tweet = form.save(commit=False)
                tweet.user = request.user
                tweet.save()
                messages.success(request, ('Your Tweet Has Benn Sent'))
                return redirect('home')
        tweets = Tweet.objects.all().order_by('-created_at')
        return render(request, 'home.html', {"tweets": tweets, 'form': form})
    else:
        tweets = Tweet.objects.all().order_by('-created_at')
        return render(request, 'home.html', {"tweets": tweets})


def profile_list(request):
    if request.user.is_authenticated:
        profile = Profile.objects.exclude(user=request.user)
        return render(request, 'profile_list.html', {"profiles": profile})
    else:
        messages.success(request, ("You Must Be Logged In To View This Page"))
        return redirect('home')


def profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        tweets = Tweet.objects.filter(user_id=pk)
        # Form Part
        if request.method == "POST":
            # GET CURRENT USER
            current_user_profile = request.user.profile
            # GET FORM DATA
            action = request.POST['follow']
            # FOLLOW OR UNFOLLOW DECISION
            if action == 'unfollow':
                current_user_profile.follows.remove(profile)
            elif action == 'follow':
                current_user_profile.follows.add(profile)
            # SAVE THE PROFILE
            current_user_profile.save()

        return render(request, 'profile.html', {'profile': profile, 'tweets': tweets})
    else:
        messages.success(request, ("You Must Be Logged In To View This Page"))
        return redirect('home')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("Successfully Logged In"))
            return redirect('home')
        else:
            messages.success(request, ("There was an Error Logging in Please Try Again"))
            return redirect('home')
    return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, ("You Have Been Loged our"))
    return redirect('home')


def register(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, ("Wellcome !!! Successfully Signed Up"))
            return redirect('home')
    return render(request, 'register.html', {'form': form})

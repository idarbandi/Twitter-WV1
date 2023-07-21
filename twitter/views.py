from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile, Tweet
from django.contrib import messages
from .forms import TweetForm, SignUpForm, ProfilePicForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
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


def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        profile_user = Profile.objects.get(user__id=request.user.id)
        user_form = SignUpForm(request.POST or None, request.FILES or None, instance=current_user)
        profile_form = ProfilePicForm(request.POST or None, request.FILES or None, instance=profile_user)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            login(request, current_user)
            messages.success(request, ("Your Profile Has Been Updated"))
            return redirect('home')
        return render(request, 'update_user.html', {'user_form': user_form, 'profile_form': profile_form})
    else:
        messages.success(request, ("You Must Be Logged in to View This Page"))
        return redirect('home')


def tweet_likes(request, pk):
    if request.user.is_authenticated:
        tweet = get_object_or_404(Tweet, id=pk)
        if tweet.likes.filter(id=request.user.id):
            tweet.likes.remove(request.user)
        else:
            tweet.likes.add(request.user)
        return redirect(request.META('HTTP_REFERER'))
    else:
        messages.success(request, ("You Must Be Logged in to View This Page"))
        return redirect('home')


def tweet(request, pk):
    tweet = get_object_or_404(Tweet, id=pk)
    if tweet:
        return render(request, 'single.html', {'tweet': tweet})
    else:
        messages.success(request, ("Tweet Does Not Exist"))
        return redirect('home')


def unfollow(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        # unfollow
        request.user.profile.follows.remove(profile)
        request.user.profile.save()
        messages.success(request, (f'You Unfollwed {profile.user.username}'))
        return redirect('home')

    else:
        messages.success(request, ("You Must Be Logged in to View This Page"))
        return redirect('home')

from django.shortcuts import render, redirect
from .models import Profile, Tweet
from django.contrib import messages


def home(request):
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

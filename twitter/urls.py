from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('profile_list', views.profile_list, name='profile_list'),
    path('profile/<int:pk>', views.profile, name='profile'),
    path('profile/followers/<int:pk>', views.followers, name='followers'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.register, name='register'),
    path('update_user', views.update_user, name='update_user'),
    path('tweet_likes/<int:pk>', views.tweet_likes, name='tweet_likes'),
    path('tweet/<int:pk>', views.tweet, name='tweet'),
    path('unfollow/<int:pk>', views.unfollow, name='unfollow'),
    path('follow/<int:pk>', views.follow, name='follow')
]
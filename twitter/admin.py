from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile

# Unregister Groups
admin.site.unregister(Group)


# Mix Profile Info Into User Info
class ProfileInline(admin.StackedInline):
    model = Profile


# Extend User Model
class UserAdmin(admin.ModelAdmin):
    model = User
    # Just Display Username On Admin Pages
    fields = ["username"]
    inlines = [ProfileInline]


# Unregister Initial User
admin.site.unregister(User)

# Resgister User & Profiles
admin.site.register(User, UserAdmin)
admin.site.register(Profile)
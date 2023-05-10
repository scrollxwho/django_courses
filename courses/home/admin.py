from django.contrib import admin
from django.contrib.auth.models import User
from .models import Course

# class UserAdmin(admin.ModelAdmin):
#     list_display = ['password', 'username']
#
# # admin.site.register(User, UserAdmin)

admin.site.register(Course)
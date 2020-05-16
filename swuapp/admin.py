from django.contrib import admin
from .models import Lecture, UserLecture, Board,Profile, Student_User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.

admin.site.register(Lecture)
admin.site.register(UserLecture)
admin.site.register(Board)
admin.site.register(Student_User)

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
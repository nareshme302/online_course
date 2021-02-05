from django.contrib import admin

# Register your models here.
from .models import Lesson,Course,Subscription,UserMembership,Membership

admin.site.register(Lesson)
admin.site.register(Course)
admin.site.register(Subscription)
admin.site.register(UserMembership)
admin.site.register(Membership)
from django.urls import path
from . import views


urlpatterns=[
    path("course/",views.home,name="home"),
    path("course/<int:course_id>/",views.course_details,name="course_details"),
    path("course/<int:course_id>/<int:lesson_id>/", views.lesson_details, name="lesson_details"),
    path("membership/",views.course_membership,name="course_membership"),
    path("signin/",views.user_signup),
    path("login/",views.user_login),
    path("logout/", views.user_logout),
]
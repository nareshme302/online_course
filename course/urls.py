from django.urls import path
from . import views


urlpatterns=[
    path("course/",views.home,name="home"),
    path("course/<int:course_id>/",views.course_details,name="course_details"),
    path("course/<int:course_id>/<int:lesson_id>/", views.lesson_details, name="lesson_details"),
    path("membership/<int:m_id>/",views.course_membership,name="course_membership"),
]


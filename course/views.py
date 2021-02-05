from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect, get_object_or_404, get_list_or_404
from .models import Lesson, Course, Subscription, UserMembership, Membership


# Create your views here.
def home(request):
    courses = get_list_or_404(Course)
    return render(request, "course.html", {"courses": courses})


def course_details(request, course_id):
    # breakpoint()
    course = Course.objects.get(id=course_id)
    m_type = course.allowed_membership.all()
    lessons = course.lesson_set.all()
    return render(request, "course_details.html", {"course": course, "lessons": lessons, "type": m_type})


def lesson_details(request, course_id, lesson_id):
    course = Course.objects.get(id=course_id)
    lesson = course.lesson_set.get(id=lesson_id)
    return render(request, "lesson_details.html", {"lesson": lesson})


def course_membership(request,m_id):
    memberships = Membership.objects.get(id=m_id)
    membership_courses= memberships.course_set.all()
    return render(request,"course_membership.html",{"membe":memberships,"membership_courses":membership_courses})
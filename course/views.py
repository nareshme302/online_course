from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect, get_object_or_404, get_list_or_404
from .models import Lesson, Course, Subscription, UserMembership, Membership
from django.contrib.auth.models import User


# Create your views here.
@login_required(login_url='/login/')
def home(request):
    courses = get_list_or_404(Course)
    return render(request, "course.html", {"courses": courses})


@login_required(login_url='/login/')
def course_details(request, course_id):
    # breakpoint()
    course = Course.objects.get(id=course_id)
    m_type = course.allowed_membership.all()
    lessons = course.lesson_set.all()
    return render(request, "course_details.html", {"course": course, "lessons": lessons, "type": m_type})


@login_required(login_url='/login/')
def lesson_details(request, course_id, lesson_id):
    course = Course.objects.get(id=course_id)
    lesson = course.lesson_set.get(id=lesson_id)
    return render(request, "lesson_details.html", {"lesson": lesson})


@login_required(login_url='/login/')
def course_membership(request):
    member_ships = Membership.objects.all()
    return render(request, "course_membership.html", {"memberships": member_ships})

























































def user_signup(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/course/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login/')
        else:
            return render(request, 'signin.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'signin.html', {'form': form})


def user_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/course/")
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/course/')
        else:
            form = AuthenticationForm(request.POST)
            return render(request, 'login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

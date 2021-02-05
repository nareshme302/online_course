from django.db import models
from django.contrib.auth.models import User

# Create your models here.
MEMBERSHIP_TYPE = (("FREE", "free"),
                   ("PRO", "pro"),
                   ("ENTERPRISE", "enterprise"))


class Membership(models.Model):
    type = models.CharField(max_length=15, default="free", choices=MEMBERSHIP_TYPE)
    price = models.IntegerField()
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.type


class UserMembership(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    membership_type = models.ForeignKey(Membership, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Subscription(models.Model):
    user_membership = models.ForeignKey(UserMembership, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.user_membership.user.username


class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    allowed_membership = models.ManyToManyField(Membership)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    title = models.CharField(max_length=150)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    video = models.FileField(upload_to="media/videos/", null=True, blank=True)
    image = models.ImageField(upload_to="media/images/",blank=True,null=True)

    def __str__(self):
        return self.title

from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class Course(models.Model):
    name = models.CharField(max_length=50, unique=True)
    describe = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def get_absolute_url(self):
        return f'/category/{self.id}'


class Mentor(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)


class Student(AbstractUser):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="users/%Y/%m/%d", blank=True)
    birthday = models.DateField(blank=True, null=True)
    password = models.CharField(_("password"), max_length=500, blank=True)

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"


class Content(models.Model):
    name = models.CharField(max_length=255)
    video_lesson = models.URLField()
    description = models.TextField()
    documentation = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class Task(models.Model):
    name = models.TextField()
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class Solution(models.Model):
    description = models.TextField()
    student_id = models.IntegerField()
    solution_url = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE)



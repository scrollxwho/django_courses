from django.shortcuts import render
from django.views import View
from rest_framework import generics
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from api.serializers import CourseSerializer
from home.models import Course


class ModelsView(generics.ListCreateAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        Course.objects.all()


class CreateCourse(generics.ListCreateAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        Course.objects.all()


class MultiTask(RetrieveUpdateDestroyAPIView):
    serializer_class = CourseSerializer

    # queryset = Course.objects.get(pk=self.pk)

    def get_queryset(self):
        Course.objects.all()

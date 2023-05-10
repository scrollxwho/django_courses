from django.shortcuts import render
from rest_framework import generics
from api.serializers import CourseSerializer
from home.models import Course


class ModelsView(generics.ListAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        Course.objects.all()


class CreateCourse(generics.ListCreateAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        Course.objects.all()
from django.urls import path
from .views import *

urlpatterns = [
    path('view/', ModelsView.as_view()),
    path('create/', CreateCourse.as_view()),
    path('course/<pk>', MultiTask.as_view()),
]
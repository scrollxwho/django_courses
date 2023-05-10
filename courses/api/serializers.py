from rest_framework import serializers
from home.models import Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'describe', 'start_date', 'end_date']

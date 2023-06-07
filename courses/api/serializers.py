from rest_framework import serializers
from home.models import Course, Teacher, Mentor, Student, Content, Solution, Task

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'describe', 'start_date', 'end_date']


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields: ['name', 'surname']


class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields: ['name', 'surname']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields: ['name', 'surname', 'course_id', 'teacher_id']


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields: ['name', 'video_lesson', 'description', 'documentation']


class SolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solution
        fields: ['description', 'task_id', 'student_id', 'solution_url']


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields: ['name']
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from course.models import Course, Lesson


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(ModelSerializer):

    class Meta:
        model = Course
        fields = "__all__"


class CourseDetailSerializer(ModelSerializer):

    lessons_count = SerializerMethodField()
    lessons = SerializerMethodField()

    def get_lessons_count(self, course):
        return Lesson.objects.filter(course=course).count()

    def get_lessons(self, course):
        return Lesson.objects.filter(course=course).values("name", "description", )


    class Meta:
        model = Course
        fields = ('name', 'description', 'lessons_count', 'lessons')






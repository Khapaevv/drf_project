from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from course.models import Course, Lesson


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(ModelSerializer):
    # lessons = LessonSerializer(many=True, read_only=True, source='lesson_set')
    class Meta:
        model = Course
        fields = "__all__"


class CourseDetailSerializer(ModelSerializer):

    lessons_count = SerializerMethodField()
    # lessons = LessonSerializer(many=True, read_only=True, source='lesson_set')
    def get_lessons_count(self, course):
        return Lesson.objects.filter(course=course).count()


    class Meta:
        model = Course
        fields = ('name', 'description', 'lessons_count')
        # fields = ('name', 'description', 'lessons_count', 'lessons')






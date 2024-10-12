from rest_framework import serializers
from course.models import Course, Lesson
from course.validators import validate_normal_link


class LessonSerializer(serializers.ModelSerializer):
    video = serializers.URLField(validators=[validate_normal_link], required=False, allow_blank=True, allow_null=True)

    class Meta:
        model = Lesson
        fields = "__all__"



class CourseSerializer(serializers.ModelSerializer):

    lessons_count = serializers.SerializerMethodField()
    lessons = serializers.SerializerMethodField()

    def get_lessons_count(self, course):
        return Lesson.objects.filter(course=course).count()

    def get_lessons(self, course):
        return Lesson.objects.filter(course=course).values(
            "name",
            "description",
        )

    class Meta:
        model = Course
        fields = ("name", "description", "lessons_count", "lessons")

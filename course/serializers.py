from rest_framework.serializers import ModelSerializer, SerializerMethodField

from course.models import Course, Lesson


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class LessonSerializer(ModelSerializer):

    class Meta:
        model = Lesson
        fields = "__all__"

class LessonDetailSerializer(ModelSerializer):
    lessons_count = SerializerMethodField()

    def get_lessons_count(self, lesson):
        return Lesson.objects.all().count

    class Meta:
        model = Lesson
        fields = ("name", "description", "lessons_count")

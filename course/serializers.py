from rest_framework import serializers

from course.models import Course, Lesson, Subscription
from course.validators import validate_normal_link


class LessonSerializer(serializers.ModelSerializer):
    video = serializers.URLField(
        validators=[validate_normal_link],
        required=False,
        allow_blank=True,
        allow_null=True,
    )

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):

    lessons_count = serializers.SerializerMethodField()
    lessons = serializers.SerializerMethodField()
    is_subscribed = serializers.SerializerMethodField(read_only=True)

    def get_lessons_count(self, course):
        return Lesson.objects.filter(course=course).count()

    def get_lessons(self, course):
        return Lesson.objects.filter(course=course).values(
            "name",
            "description",
        )

    def get_subscription(self, course):
        user = self.context['request'].user
        return Subscription.objects.all().filter(user=user).filter(course=course).exists()


    class Meta:
        model = Course
        fields = ("name", "description", "lessons_count", "lessons", "subscription")

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'

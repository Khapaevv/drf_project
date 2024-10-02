from django.urls import path
from rest_framework.routers import SimpleRouter

from course.apps import CourseConfig
from course.views import (LessonViewSet, CourseListAPIView, CourseRetrieveAPIView, CourseCreateAPIView,
    CourseDestroyAPIView, CourseUpdateAPIView,
)

app_name = CourseConfig.name

router = SimpleRouter()
router.register("", LessonViewSet)



urlpatterns = [
    path("course/", CourseListAPIView.as_view(), name="course_view"),
    path("course/<int:pk>/", CourseRetrieveAPIView.as_view(), name="course_retrieve"),
    path("course/create/", CourseCreateAPIView.as_view(), name="course_create"),
    path("course/<int:pk>/delete/", CourseDestroyAPIView.as_view(), name="course_delete"),
    path("course/<int:pk>/update/", CourseUpdateAPIView.as_view(), name="course_update"),
]
urlpatterns += router.urls

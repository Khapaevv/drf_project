from django.contrib import admin

from course.models import Course, Lesson


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "preview", "description")
    list_filter = ("name",)
    search_fields = ("name",)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "preview", "description", "video", "course")
    list_filter = (
        "name",
        "course",
    )
    search_fields = (
        "name",
        "course",
    )

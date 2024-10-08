from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("course/", include("course.urls", namespace="course")),
    path("user/", include("users.urls", namespace="user")),
    path("payments/", include("payments.urls", namespace="payments")),
]

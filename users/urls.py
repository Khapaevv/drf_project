from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# from course.views import CourseCreateAPIView, CourseListAPIView, CourseRetrieveAPIView, CourseUpdateAPIView, CourseDestroyAPIView
from users.apps import UsersConfig
from users.views import PaymentsViewSet, UserViewSet, UserCreateApiView

# from course.views import (LessonViewSet)


app_name = UsersConfig.name

router_payments = SimpleRouter()
router_payments.register("payments/", PaymentsViewSet)

router_users = SimpleRouter()
router_users.register("", UserViewSet)

urlpatterns = [
    path('register/', UserCreateApiView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh'),
]


urlpatterns += router_users.urls
urlpatterns += router_payments.urls

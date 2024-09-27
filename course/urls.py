from rest_framework.routers import SimpleRouter

from course.views import CourseViewSet
from course.apps import CourseConfig

app_name = CourseConfig.name

router = SimpleRouter()
router.register("", CourseViewSet)


urlpatterns = []
urlpatterns += router.urls

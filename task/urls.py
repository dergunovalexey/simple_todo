from rest_framework.routers import DefaultRouter

from task.views import ToDoViewSet


router = DefaultRouter()
router.register(r'todos', ToDoViewSet, basename='todo')

urlpatterns = router.urls

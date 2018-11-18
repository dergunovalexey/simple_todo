from django.urls import path, include
from rest_framework.routers import DefaultRouter

from userdata.views import UserViewSet


router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('auth/', include('rest_framework.urls')),
]

urlpatterns += router.urls

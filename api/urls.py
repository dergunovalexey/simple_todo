from django.urls import path, include


urlpatterns = [
    path('tasks/', include('task.urls')),
    path('userdata/', include('userdata.urls')),
]

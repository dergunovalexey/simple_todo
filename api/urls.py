from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='ToDo API')

urlpatterns = [
    path('tasks/', include('task.urls')),
    path('userdata/', include('userdata.urls')),
    path('docs/', schema_view),
]

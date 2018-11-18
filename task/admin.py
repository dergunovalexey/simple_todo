from django.contrib import admin

from task.models import ToDo


@admin.register(ToDo)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'priority')
    list_filter = ('status', 'priority', 'created_at', 'updated_at')

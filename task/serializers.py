from rest_framework import serializers

from task.models import ToDo


class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ('id', 'user', 'title', 'description', 'status', 'priority',
                  'created_at', 'updated_at', 'created_by', 'updated_by')
        read_only_fields = (
            'id', 'created_at', 'updated_at', 'created_by', 'updated_by')

from django.db import models


class StatusesToDo:
    WAIT = 100
    IN_PROGRESS = 200
    DONE = 300
    FATAL = 400

    CHOICES = (
        (WAIT, 'wait'),
        (IN_PROGRESS, 'in progress'),
        (DONE, 'done'),
        (FATAL, 'fatal'),
    )


class Priorities:
    LOW = 100
    DEFAULT = 200
    HIGH = 300

    CHOICES = (
        (LOW, 'low'),
        (DEFAULT, 'default'),
        (HIGH, 'high'),
    )


class ToDo(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    status = models.PositiveSmallIntegerField(
        choices=StatusesToDo.CHOICES, default=StatusesToDo.WAIT)
    priority = models.PositiveSmallIntegerField(
        choices=Priorities.CHOICES, default=Priorities.DEFAULT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, related_name='creator')
    updated_by = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, related_name='updater')

    def __str__(self):
        return f'Some todo {self.id}'

from django.db import models

class Task(models.Model):
    STATUS_CHOICES = [
        ('not_started', 'Yet to Start'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not_started')
    in_progress = models.BooleanField(default=False)

    def __str__(self):
        return self.title

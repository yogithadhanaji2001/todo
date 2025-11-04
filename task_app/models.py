from django.db import models

# Create your models here.


from user_app.models import User

class TaskManager(models.Model):

    priority_choice = [('low','low'),
                       ('high','high'),
                       ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    priority= models.CharField(max_length=30, choices=priority_choice)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True,)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
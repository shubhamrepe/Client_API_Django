from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    client_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='clients_created', on_delete=models.CASCADE)

    def __str__(self):
        return self.client_name
from django.db import models

class Project(models.Model):
    project_name = models.CharField(max_length=255)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    users = models.ManyToManyField(User)
    created_by = models.ForeignKey(User, related_name='created_projects', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project_name

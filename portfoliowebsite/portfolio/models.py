from django.db import models
import random

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=25, null=False)
    short_description = models.CharField(max_length=200, null=False)
    long_description = models.TextField(blank=True)
    github_link = models.URLField(blank=True)

    project_status_choices = [('complete', 'complete'), ('incomplete', 'incomplete')]
    status = models.CharField(max_length=10, default='incomplete', choices=project_status_choices)

    def __str__(self):
        return self.project_name
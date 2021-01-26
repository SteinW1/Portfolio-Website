from django.db import models

class Project(models.Model):
    project_name = models.CharField(max_length=25, unique=True, null=False)
    description = models.TextField()

    def __str__(self):
        return self.project_name
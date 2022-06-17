from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.TextField()
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    url = models.URLField()
    tags = models.TextField()

    def __str__(self):
        return self.title


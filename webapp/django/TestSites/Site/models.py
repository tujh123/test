from django.db import models

class Site(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.title + ' | ' + self.description
import datetime
from django.db import models

class Work(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(default=datetime.datetime.now())
    description = models.TextField(null=False,blank=False)

    def __str__(self):
        return self.title

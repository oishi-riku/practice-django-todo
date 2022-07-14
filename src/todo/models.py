from django.db import models

class TodoModel(models.Model):
    title = models.CharField(max_length=100, default='')
    memo = models.TextField(null=True)

    def __str__(self):
        return self.title
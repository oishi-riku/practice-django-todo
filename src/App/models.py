from django.db import models

class TodoModel(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=2000)
    owner = models.ForeignKey('auth.User', related_name='todo', on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title

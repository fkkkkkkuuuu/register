
from django.db import models


class UserTask(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='task_images/')
    task = models.TextField()

    def __str__(self):
        return self.title




    class Meta:
        verbose_name = "example"
        verbose_name_plural = "examples"
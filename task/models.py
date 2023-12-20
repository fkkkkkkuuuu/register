from django.db import models






class Task(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='task_images/')
    task_description = models.TextField()


    def __str__(self):
        return self.title

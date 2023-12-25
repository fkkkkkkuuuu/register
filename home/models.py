from django.db import models


class StringRun(models.Model):
    title_text = models.CharField(max_length=100, verbose_name='Enter your title text')
    description_text = models.TextField(verbose_name='Enter your description text')

    def __str__(self):
        return self.title_text


    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'

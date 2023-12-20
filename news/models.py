from django.db import models


class EventModel(models.Model):
    GENRE = (
        ('IDO', 'Listing'),
        ('Byvotes', 'Airdrop')
    )
    title = models.CharField('Название', max_length=100)
    description = models.TextField('Описание')
    image = models.ImageField(upload_to='events/', verbose_name='Изображение')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

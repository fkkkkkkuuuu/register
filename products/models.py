from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Ценник')
    image = models.ImageField(upload_to='product_images/', verbose_name='Изображение')
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления',null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


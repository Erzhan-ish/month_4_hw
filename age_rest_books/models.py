from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Books(models.Model):
    name = models.CharField(max_length=100, verbose_name='Введите название')
    price = models.FloatField(default=100, verbose_name='Задайте цену')
    tags = models.ManyToManyField(Tag)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.name
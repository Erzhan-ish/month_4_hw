from django.db import models
from library_blog.models import BookModel

class BasketModel(models.Model):
    name = models.CharField(max_length=100, verbose_name='Введите имя')
    email = models.EmailField(verbose_name='Укажите эл.почту ')
    phone_number = models.IntegerField(verbose_name='Введите номер телефона')
    book = models.URLField(verbose_name='Укажите ссылку аудио книги')
    book_buy = models.ForeignKey(BookModel, on_delete=models.CASCADE, related_name='buy_book', null=True)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
from django.db import models

class BookModel(models.Model):
    GENRE = (
        ('Хоррор', 'Хоррор'),
        ('Комедия', 'Комедия'),
        ('Детектив', 'Детектив')
    )
    image = models.ImageField(upload_to='books/', verbose_name='Загрузите фото Книги')
    title = models.CharField(max_length=100, verbose_name='Укажите название книги')
    description = models.TextField(verbose_name='Укажите описание', blank=True)
    price = models.FloatField(verbose_name='Задайте цену книги', default=25)
    created_at = models.DateField(auto_now_add=True)
    genre = models.CharField(max_length=100, choices=GENRE, default='Детектив')
    author_gmail = models.EmailField(verbose_name='Укажите эл.почту автора')
    author = models.CharField(max_length=100, verbose_name='Укажите автора', default='Туратбеков алибек')
    audio_book = models.URLField(verbose_name='Укажите ссылку аудио книги')


    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.title

class Review(models.Model):
    POINTS = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),

    )
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE, related_name='reviews')
    created_at = models.DateField(auto_now_add=True)
    text_review = models.TextField(verbose_name='Напишите отзыв о книге')
    points = models.CharField(max_length=100, verbose_name="Поставьте оценку", choices=POINTS, default='1')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return F'{self.book} - {self.points}'
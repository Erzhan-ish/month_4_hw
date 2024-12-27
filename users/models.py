from django.db import models
from django.contrib.auth.models import User

class CustomUser(User):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    level = models.CharField(max_length=15, verbose_name='Ваш уровень (jun/middle/senior)')
    age = models.PositiveIntegerField(default=18)
    gender = models.CharField(max_length=10, choices=GENDER, default='Male')
    salary = models.CharField(max_length=100, default='ЗП не определен')

    def save(self, *args, **kwargs):
        if self.level == 'jun':
            self.salary = '700$'
        elif self.level == 'middle':
            self.salary = '1000$'
        elif self.level == 'senior':
            self.salary = '2000$'
        else:
            self.club = 'Пожалуста подтяните ваш уровень'

        super().save(*args, **kwargs)
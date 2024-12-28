from django.db import models


class RecipeModel(models.Model):
    title = models.CharField(max_length=20, verbose_name="Название рецепта")
    description = models.TextField(verbose_name="Описание рецепта")

    def __str__(self):
        return self.title


class IngredientModel(models.Model):
    UNIT = (
        ('Kилограммы', 'Kилограммы'),
        ('Граммы', 'Граммы'),
        ('Литры', 'Литры'),
        ('Миллилитры', 'Миллилитры'),
        ('Штуки', 'Штуки')
    )
    name = models.CharField(max_length=30, verbose_name='Название ингредиента')
    quantity = models.IntegerField(verbose_name='Количество')
    unit = models.CharField(max_length=30, choices=UNIT)
    recipe = models.ForeignKey(RecipeModel, on_delete=models.CASCADE, related_name='recipe')

    def __str__(self):
        return self.name

class CollectionModel(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название коллекции')
    recipes = models.ManyToManyField(RecipeModel)

    def __str__(self):
        return self.name
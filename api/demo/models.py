from django.db import models


class Weapon(models.Model):
    power = models.IntegerField()
    rarity = models.CharField(max_length=50)
    value = models.IntegerField()

# после создания модели: создаем миграцию (makemigrations) и применяем её (migrate)

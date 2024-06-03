from rest_framework import serializers

from demo.models import Weapon


# class WeaponSerializer(serializers.Serializer):  # создаем сериализатор без импорта модели Weapon
#     power = serializers.IntegerField()           # описываем свойства, которые д/б сконвертированы в json, и наоброт из json в сложный объект: указываем какие поля из модели отображать
#     rarity = serializers.CharField()

#  если сериализатор повторяет вид модели, то использовать специальный сериализатор .ModelSerializer, который требует указания на основании какой модели создается сериализатор
class WeaponSerializer(serializers.ModelSerializer):   # создаем сериализатор для модели Weapon
    class Meta:               # внутренний класс для указания модели, на основании которой строится сериализатор
        model = Weapon                # не забывать импортировать модель
        fields = ['id', 'power', 'rarity']  # указываем какие свойства из модели необходимо отображать

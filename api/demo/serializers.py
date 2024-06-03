from rest_framework import serializers

from demo.models import Weapon


# class WeaponSerializer(serializers.Serializer):  # создаем сериализатор без импорта модели Weapon
#     power = serializers.IntegerField()
#     rarity = serializers.CharField()


class WeaponSerializer(serializers.ModelSerializer):   # создаем сериализатор для модели Weapon
    class Meta:               # описываем свойства, которые д/б сконвертированы в json, и наоброт из json в сложный объект
        model = Weapon
        fields = ['id', 'power', 'rarity']

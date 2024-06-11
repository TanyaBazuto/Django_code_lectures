from rest_framework import serializers

from demo.models import Adv


class AdvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adv
        fields = ['id', 'user', 'text', 'created_at', 'open']   # поля, которые необходимо отоброжать у json
        read_only_fields = ['user',]                            # указываем, что поле user только для чтения, в запросах DRF берет его по токену и нам не нужно его передавать

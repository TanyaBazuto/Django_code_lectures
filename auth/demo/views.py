from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle
from rest_framework.viewsets import ModelViewSet

from demo.models import Adv
from demo.permissions import IsOwnerOrReadOnly
from demo.serializers import AdvSerializer


class AdvViewSet(ModelViewSet):
    queryset = Adv.objects.all()
    serializer_class = AdvSerializer
    permission_classes = [IsOwnerOrReadOnly]        # настройка по разделению прав пользователей, в которую мы передаем те разрешения, что требуются для работы
    throttle_classes = [AnonRateThrottle]

    def perform_create(self, serializer):           # метод есть на все действия, _create, _update, _destroy,
        serializer.save(user=self.request.user)     # вызываем сериалайзер который сохраняет объект в БД - полььзователя доостаем из запроса по токену, чтоб не указывать при запросах явно его id

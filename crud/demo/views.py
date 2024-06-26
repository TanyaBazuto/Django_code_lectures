from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet     # импортируем ViewSet

from demo.models import Comment
from demo.serializers import CommentSerializer

### Класс ViewSet для создания одного обрабочика, а не нескольких отдельных (для создания комментария, просмотра, удаления и т.д.). ViewSet позволяет сразу описать весь ресурс и все обработчики для работы с этим ресурсом.

class CommentViewSet(ViewSet):
    # метод для получения списка объектов
    def list(self, request):
        return Response({'status': 'OK"})

    # метод для получения конкретного объекта
    def retrive(self, request):
        pass

    # метод для удаления объекта
    def destroy(self, request):
        pass

    # метод для обновления объекта
    def update(self, request):
        pass

    # метод для создания объекта
    def create(self, request):
        pass


### В DRF есть более удобный ModelViewSet -- в нем уже реализованы методы ViewSet: 

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()               # атрибут "ЧТО ДОСТАЕМ" -- откуда будем брать все данные
    serializer_class = CommentSerializer               # атрибут "В КАКОМ ФОРМАТЕ ОТДАЁМ" -- сериализатор, с помощью которого все объекты будут превращаться в JSON и обратно
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]               # 2ой вариант настройка фильтров -- указание фильтров без прописывания REST_FRAMEWORK в settings.py
    filterset_fields = ['user',]                                                        # DjangoFilterBackend - список атрибутов/полей по которым выполняется фильтрация
    search_fields = ['text',]                                                           # SearchFilter -поиск по полю. Указываем поля по которым осуществляется поиск
    ordering_fields = ['id', 'user', 'text', 'created_at']                              # OrderingFilter - упорядочивание данных. Указываем список параметров по которым необходимо упорядочивание = поля по которым можно фильтровать
    pagination_class = LimitOffsetPagination                                            # 2ой вариант настройка пагинации -- указание (без прописывания в секции REST_FRAMEWORK в settings.py) pagination class для конкретного ViewSet/
(                                                                                       # Например, класс пагинации "LimitOffsetPagination" требует указания в запросе параметров: limit(сколько объектов показать за раз) и offset (сколько пропустить их)


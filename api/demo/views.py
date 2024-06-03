from django.shortcuts import render
from rest_framework.decorators import api_view        # импорт api-обработчика
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Weapon                             # подключаем необходимы модели из models.py
from .serializers import WeaponSerializer              # ипортируем сериализатор

ВАРИАНТ 1: разграничения работы методов GET и POST c использованием условий if:
# @api_view(['GET', 'POST'])                           # декоратор для превращения обработчика в api-обработчик. В () - список запросов, на которые должен отвечать обработчик
# def demo(request):                                   # не забывать регистрировать в  urls.py, и применять миграции - migrate 
#     if request.method == 'GET':                      # код для обработки GET-запросов
#         weapons = Weapon.objects.all()               # достать из БД все объекты модели Weapon  
#         ser = WeaponSerializer(weapons, many=True)   # создаем сериализованный набор данных модели Weapon с помощью сериализатора, созданного в файле serializers.py. many=True означает, что серализатор выдаст полный список объектов, а не конкретный объект
#         return Response(ser.data)
#     if request.method == 'POST':                     # код для обработки POST-запросов
#         return Response({'status': 'OK'})
.
ВАРИАНТ 2: разграничение запросов GET и POST с помощью APIView (не забывать импортировать). НО в urls.py можно регистрировать только функции, а не целый класс: поэтому в urls.py импорт: DemoView, а в path использовать метод .as_view() - ('demo/', DemoView.as_view())
# class DemoView(APIView):
#     def get(self, request):
#         weapons = Weapon.objects.all()
#         ser = WeaponSerializer(weapons, many=True)
#         return Response(ser.data)
#
#     def post(self, request):
#         return Response({'status': 'OK'})
:
ListAPIView - специальный класс для упрощения кода. По умолчанию ListAPIView формирует только GET-запрос. Остальное необходимо прописывать отдельно
class DemoView(ListAPIView):
    queryset = Weapon.objects.all()       # queryset показывает откуда брать данные
    serializer_class = WeaponSerializer   # указываем с помощью чего набор данных превратить в json

    def post(self, request):
        return Response({'status': 'OK'})

RetrieveAPIView - специальный класс для получения информации по одной конкретной записи в БД
class WeaponView(RetrieveAPIView):
    queryset = Weapon.objects.all()      # что достаем? -- поиск среди всех записей в БД
    serializer_class = WeaponSerializer  # в каком формате
Затем регистрируем маршрут обработчика WeaponView в urls.py

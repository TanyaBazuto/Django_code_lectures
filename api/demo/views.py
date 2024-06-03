from django.shortcuts import render
from rest_framework.decorators import api_view      # импорт api-обработчика
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Weapon                # подключаем необходимы модели из models.py
from .serializers import WeaponSerializer  # ипортируем сериализатор


# @api_view(['GET', 'POST'])     # декоратор для превращения обработчика в api-обработчик. В () - список запросов, на которые должен отвечать обработчик
# def demo(request):             # не забывать регистрировать в  urls.py, и применять миграции - migrate
#     if request.method == 'GET':
#         weapons = Weapon.objects.all()          # достать из БД все объекты модели Weapon  
#         ser = WeaponSerializer(weapons, many=True)   # создаем сериализованный набор данных модели Weapon с помощью сериализатора, созданного в файле serializers.py. many=True означает, что серализатор выдаст полный список объектов, а не конкретный объект
#         return Response(ser.data)
#     if request.method == 'POST':
#         return Response({'status': 'OK'})


# class DemoView(APIView):
#     def get(self, request):
#         weapons = Weapon.objects.all()
#         ser = WeaponSerializer(weapons, many=True)
#         return Response(ser.data)
#
#     def post(self, request):
#         return Response({'status': 'OK'})


class DemoView(ListAPIView):
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer

    def post(self, request):
        return Response({'status': 'OK'})


class WeaponView(RetrieveAPIView):
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer

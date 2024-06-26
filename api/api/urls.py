"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from demo.views import DemoView, WeaponView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('demo/', demo),
    path('demo/', DemoView.as_view()),             # метод .as_view() применяется при использовании в обработчике APIView
    path('weapon/<pk>/', WeaponView.as_view()),    # так как WeaponView - это запрос на конкретную запись в БД, то в маршруте регистриуем id записи - <pk> (сокращение от primary key)
]

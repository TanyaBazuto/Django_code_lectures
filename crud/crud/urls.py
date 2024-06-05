"""crud URL Configuration

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
from rest_framework.routers import DefaultRouter

from demo.views import CommentViewSet

### ViewSet нельзя просто превратить в функцию, т.к. это набор сразу нескольких обработчиков. Для этого используем РОУТЕР- специальный класс, который умеет регистрировать маршруты для ViewSet

r = DefaultRouter()                       # стандартный роутер
r.register('comments', CommentViewSet)    # в роутере регистрируем конкретный ViewSet. Префикс 'comments'- означает по какокому url из браузера будем получать доступ к ресурсу. 

urlpatterns = [
    path('admin/', admin.site.urls),
] + r.urls                                # добавляем в существующие маршруты из роутера

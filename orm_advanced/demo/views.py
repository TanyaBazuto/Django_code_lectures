from django.shortcuts import render

from demo.models import Order


def list_orders(request):
    orders = Order.objects.filter(positions__product__price__lte=600)    #формируем список заказов. Если все заказы, то orders = Order.objects.all()
    context = {'orders': orders}                      # в context передаем все заказы из БД 
    return render(request, 'orders.html', context)    #возвращаем шаблон - генерируем с помощью шаблона новый html-код

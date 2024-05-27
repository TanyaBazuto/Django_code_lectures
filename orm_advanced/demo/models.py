from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.CharField(max_length=50)


class Order(models.Model):
    # products = models.ManyToManyField(Product, related_name='orders')  #установление связи многие-ко-иногим. related_name - чтоб можно было обратиться к продуктам из заказа
    pass   # убираем, чтоб в панели администратора не дублировалось


#ПРОМЕЖУТОЧНАЯ ТАБЛИЦА/МОДЕЛЬ в БД (в данном случае - для утсановления количества продуктов в заказе), которая будет отвечать за одну позицию в заказе, Т.Е. связывает Продукт и Заказ
class OrderPosition(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='positions') #related_name - для получения позиций в которых он участвует    
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='positions')
    quantity = models.IntegerField()    #производное поле. не связанное

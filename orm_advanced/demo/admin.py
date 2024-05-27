from django.contrib import admin
from .models import Product, Order, OrderPosition

#Inline-модели - специальный механизм, позволяющий встраивать в текущее отображение(таблицу) другое отображение
class OrderPositionInline(admin.TabularInline):     #есть admin.StackedInline - отличается внешним видом
    model = OrderPosition            # =для какой модели из models.py
    extra = 0                        # необязательный параметр, по умолчанию = 3 - сколько строк создастся в панели администратора


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'price']
    list_filter = ['category']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id']
    inlines = [OrderPositionInline, ]   # перечисляем какие инлайны использовать

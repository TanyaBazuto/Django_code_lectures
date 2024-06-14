from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):   # метод проверяет права на конкретный объект
        if request.method == 'GET':
            return True
        return request.user == obj.user                    # совпадает ли пользователь, пославший запрос на работу с ресурсом, и пользователь создавший этот ресурс

    ### метод, который означет
    # def has_permission -- метод проверки имеет ли пользователь на работу с ресурсом в целом, т.е. создание или просмотр всего ресурса. По умолчанию возвращает True

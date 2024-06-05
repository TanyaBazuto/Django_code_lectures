from django.contrib.auth.models import User
from django.db import models

# User - стандартная модель джанго, как и Group. Не забывать импортировать
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)     # on_delete - при удалении пользователя, все его комментарии удаляются
    text = models.TextField()                                    #  TextField - не имеет ограничений по длине
    created_at = models.DateTimeField(auto_now_add=True)

# после этого создаем первого пользователя - createsuperuser. И через 'python manage.py shell' создаем объекты модели(таблицы)  и незабыть сохранить - объект.save()

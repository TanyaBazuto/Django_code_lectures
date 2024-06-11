from django.contrib.auth.models import User
from django.db import models

### Объявления от пользователей
class Adv(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    open = models.BooleanField(default=True)  # открыто или закрыто объявление. По умолчанию - открыто

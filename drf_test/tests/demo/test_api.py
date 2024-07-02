import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient         #получение клиента, который сможет отправлять запросы в наш api-сервис
from model_bakery import baker

from demo.models import Message


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def user():
    return User.objects.create_user('admin')


@pytest.fixture
def message_factory():
    def factory(*args, **kwargs):
        return baker.make(Message, *args, **kwargs)

    return factory

### СТАНДРАТНАЯ СТРУКТУРА ТЕСТА, СОСТОЯЩАЯ ИЗ ТРЁХ СЕКЦИЙ
@pytest.mark.django_db                                  #декоратор, указывающий, что наш тест будет использовать БД
def test_get_messages(client, user, message_factory):
    # Arrange - 1ая секция теста -- подготовка данных: достать и положить определенные записи БД
    messages = message_factory(_quantity=10)

    # Act - 2ая секция теста -- непосредственно тестируемый функционал: например вызов того или иного метода
    response = client.get('/messages/')

    # Assert - 2ая секция теста -- проверка, того что действие действительно выполнено корректно
    assert response.status_code == 200     #проверка статуса возврата ответа от api
    data = response.json()                 #получение содержимого ответа в json для его просмотра и проверки (например, что ответ с правильным статусом не пустой
    assert len(data) == len(messages)      #проверка что длина полученного списка значений равна списку записей в БД
    for i, m in enumerate(data):           #проверка содержимого текста messages -- обращение к данным полученным в ответе в json-файле, которые содержаться в форме словаря
        assert m['text'] == messages[i].text


@pytest.mark.django_db
def test_create_message(client, user):
    count = Message.objects.count()

    response = client.post('/messages/', data={'user': user.id, 'text': 'test text'})

    assert response.status_code == 201
    assert Message.objects.count() == count + 1

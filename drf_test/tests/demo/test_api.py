import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient         #получение клиента, который сможет отправлять запросы в наш api-сервис
from model_bakery import baker                    #pip install model_bakery - библиотека для создания рандомных данных            

from demo.models import Message

### СОЗДАНИЕ ФИКСТУР
@pytest.fixture         #чтобы избавиться от дублирования кода в тестах - ФИКСТУРЫ -- специальные ф-ции, к-е возвращают некоторое значение и мы их можем принимать в качестве аргументов в нашу тестирующую ф-цию
def client():           #функция, возвращающая клиента
    return APIClient()


@pytest.fixture         #декоратор, помечающий, что это фикстура, и теперь ее можно указывать в качестве входного аргумента в любой из нашх тестирующх функций
def user():
    return User.objects.create_user('admin')

### ФИКСТУРА ДЛЯ СОЗДАНИЯ ФАБРИКИ ОБЪЕКТОВ С ПОМОЩЬЮ библиотеки model_bakery
@pytest.fixture
def message_factory():             #создания рандомных данных, Н: большого количества сообщений, чтобы проверить как ведет себя пагинация, фильтрация и пр.функции сервера
    def factory(*args, **kwargs):       #вместо создания по одному сообщению Message.objects.create(user=user.id, text='test')
        return baker.make(Message, *args, **kwargs)

    return factory

### СТАНДРАТНАЯ СТРУКТУРА ТЕСТА, СОСТОЯЩАЯ ИЗ ТРЁХ СЕКЦИЙ
@pytest.mark.django_db                                  #декоратор, указывающий, что наш тест будет использовать БД
def test_get_messages(client, user, message_factory):   #в качестве аргументов указываем ранее написанные фикстуры
    # Arrange - 1ая секция теста -- подготовка данных: достать и положить определенные записи БД
    messages = message_factory(_quantity=10)            #_quantity - сколько объектов нужно создать            

    # Act - 2ая секция теста -- непосредственно тестируемый функционал: например вызов того или иного метода
    response = client.get('/messages/')

    # Assert - 2ая секция теста -- проверка, того что действие действительно выполнено корректно
    assert response.status_code == 200     #проверка статуса возврата ответа от api
    data = response.json()                 #получение содержимого ответа в json для его просмотра и проверки (например, что ответ с правильным статусом не пустой
    assert len(data) == len(messages)      #проверка что длина полученного списка значений равна списку записей в БД
    for i, m in enumerate(data):           #проверка содержимого текста messages -- обращение к данным полученным в ответе в json-файле, которые содержаться в форме словаря
        assert m['text'] == messages[i].text


@pytest.mark.django_db
def test_create_message(client, user):      #тест на создание сообщений 
    count = Message.objects.count()         #запрашиваем количество сообщений в БД

    response = client.post('/messages/', data={'user': user.id, 'text': 'test text'})   #напишем действие по созданию message. Для передачи в json, а не в тексте, можно здесь же +аргумент format='json'
                                                                                          # или создать настройки в settings.py  в секции REST_FRAMEWORK

    assert response.status_code == 201       #проверка что наш response вернулся с правильным кодом
    assert Message.objects.count() == count + 1   #проверяем что количество сообщений после создания (post) == изначальное количество +1

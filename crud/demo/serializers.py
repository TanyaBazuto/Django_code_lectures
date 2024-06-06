from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from demo.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    text = serializers.CharField(min_length=10)                 # ограничение длины текста -- теперь сериализатор не пропустит комментарии длиной менее 10 символов

    class Meta:                                                 # отвечает только за ПРЕДСТАВЛЕНИЕ данных из сложных python-объектов в json и обратно
        model = Comment
        fields = ['id', 'user', 'text', 'created_at']

    def validate_text(self, value):                             # ВАЛИДАЦИЯ: проверка текста на запрещенные слова. Специальный метод "validate_название поля, которое хотим провалидировать". На вход принимаем значение value
        if 'text' in value:                                     # добавление исключения, если текст не прошел проверку. В данном случае запрещенное слово -- 'text'
            raise ValidationError('Вы использовали запрещенное слово')   # не забывать импортировать ValidationError. Можно дополнительно указать 'Текст ошибки'
        return value                                            # возвращаем значение value, после прохождения всех проверок

    ### Если нам необходимо проверить комбинацию нескольких полей, не только текст, а например запрет использовать определенные слова пользователю с определенным идентификатором
    # def validate(self, attrs):                                  # def validate на вход получает все атрибуты/поля, которые были переданы при создании объекта
    #     if 'hello' in attrs['text'] or attrs['user'].id == 1:   # Например, если встречается "hello" в тексте или идентификатор пользователя - 1
    #         raise ValidationError('Что-то пошло не так')
    #     return attrs

    ### Еще одна обязанность сериализатора - СОЗДАНИЕ и ОБНОВЛЕНИЕ объектов -- как создавать объект.
    ### .ModelSerializer уже использует created_at и updated_at, но если необходимо изменить эту логику или добавить поведение, то можно переопределить данные методы и добавить свой код.
    def create(self, validated_data):          # принимает на вход validated_data, которые были получены из запроса пользователя
        print(validated_data)
        return super().create(validated_data)

# Задание 3: Отправка данных
# Используйте API, которое принимает POST-запросы для создания новых данных (например, https://jsonplaceholder.typicode.com/posts).
# Создайте словарь с данными для отправки (например, {'title': 'foo', 'body': 'bar', 'userId': 1}).
# Отправьте POST-запрос с этими данными.
# Распечатайте статус-код и содержимое ответа.
# В поле для ответа загрузи скриншоты сделанных заданий или ссылку на Git

import requests

# URL-адрес API
url = "https://jsonplaceholder.typicode.com/posts"

# Данные для отправки
data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

# Отправка POST-запроса
response = requests.post(url, data=data)

# Распечатка статус-кода и содержимого ответа
print("Статус-код:", response.status_code)
print("   ")
print("Содержимое ответа:", response.json())


# Задание 2: Параметры запроса
# Используйте API, который позволяет фильтрацию данных через URL-параметры (например, https://jsonplaceholder.typicode.com/posts).
# Отправьте GET-запрос с параметром userId, равным 1.
# Распечатайте полученные записи.

import requests

# URL-адрес API
url = "https://jsonplaceholder.typicode.com/posts"

# Параметры запроса
params = {
    "userId": 1
}

# Отправка GET-запроса
response = requests.get(url, params=params)

# Распечатка полученных записей
for post in response.json():
    print(post)


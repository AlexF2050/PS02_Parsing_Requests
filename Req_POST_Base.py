import requests

# переменная
url = "https://jsonplaceholder.typicode.com/posts"

# создаем словарь и внутри ключии значения
data = {
    "title": "тестовый пост запрос",
    "body": "тестовый контент post запросa",
    "userId": "2"
}

# отправляем запрос
response = requests.post(url, data=data)

print(response.status_code)

print(f"Ответ сервера: {response.json()}")
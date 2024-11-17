# Парсинг сайта

import requests

# запросит с сайта google информацию и сохранит её в переменную response
response = requests.get('https://www.google.com') # запросит с сайта google информацию и сохранит её в переменную response

print("выводит статус ответ - успешно или нет прошел запрос (200 -успех или 404 - не найден) ")
print(response.status_code) # выводит статус ответ - успешно или нет прошел запрос (200 -успех или 404 - не найден)
if response.ok:
    print("Ответ успешный")
else:
    print("Произошла ошибка - ответ не успешный")

print("  ")
print("выводит текст ответа ")
print(response.text) # выводит текст ответа

print("  ")
print("выводит содержимое ответа ")
print(response.content) # выводит содержимое ответа

print("  ")
print("выводит содержимое ответа ")
print(response.json) # выводит содержимое ответа файла json (Это как словарь в Python)

dict = {
    'url': 'https://www.google.com/'
}


print("  ")
print("выводит True если ответ успешный и False если нет ")
print(response.ok) # выводит True если ответ успешный и False если нет

print("  ")
print("выводит заголовки ответа ")
print(response.headers) # выводит заголовки ответа

print("  ")
print("выводит url ответа ")
print(response.url) # выводит url ответа

print("  ")
print("выводит кодировку ответа ")
print(response.encoding) # выводит кодировку ответа

print("  ")
print("выводит куки ответа ")
print(response.cookies) # выводит куки ответа

print("  ")
print("выводит историю запроса ")
print(response.history) # выводит историю запроса

print("  ")
print("выводит время ответа ")
print(response.elapsed) # выводит время ответа

print("  ")
print("выводит сырые данные ответа ")
print(response.raw) # выводит сырые данные ответа

print("  ")
print("выводит запрос ")
print(response.request) # выводит запрос

print("  ")
print("выводит причину ответа ")
print(response.reason) # выводит причину ответа

print("  ")
print("Запрос окончен")



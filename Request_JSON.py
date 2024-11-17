# Парсинг сайта json
import requests # для запросов
import pprint # для печати

# запросит с сайта google информацию и сохранит её в переменную response
response = requests.get('https://api.github.com') # запросит с сайта информацию и сохранит её в переменную response

print("Статус ответа: ")
print(response.status_code) # выводит статус ответ - успешно или нет прошел запрос (200 -успех или 404 - не найден)
if response.ok:
    print("Ответ успешный")
else:
    print("Произошла ошибка - ответ не успешный")

print("  ")
print("Выводит текст ответа text ____________________________________________________________________")
print(response.text) # выводит текст ответа с ключами и их значением
response.json = response.json() # присваивает переменной json переменную ответа
pprint.pprint(response.json) # выводит json ответа

print("  ")
print("Запрос окончен!______________________________________________________________________________!")

#
# print("  ")
# print("выводит True если ответ успешный и False если нет ")
# print(response.ok) # выводит True если ответ успешный и False если нет
#
# print("  ")
# print("выводит заголовки ответа ")
# print(response.headers) # выводит заголовки ответа
#
# print("  ")
# print("выводит url ответа ")
# print(response.url) # выводит url ответа
#
# print("  ")
# print("выводит кодировку ответа ")
# print(response.encoding) # выводит кодировку ответа
#
# print("  ")
# print("выводит куки ответа ")
# print(response.cookies) # выводит куки ответа
#
# print("  ")
# print("выводит историю запроса ")
# print(response.history) # выводит историю запроса
#
# print("  ")
# print("выводит время ответа ")
# print(response.elapsed) # выводит время ответа
#
# print("  ")
# print("выводит сырые данные ответа ")
# print(response.raw) # выводит сырые данные ответа
#
# print("  ")
# print("выводит запрос ")
# print(response.request) # выводит запрос
#
# print("  ")
# print("выводит причину ответа ")
# print(response.reason) # выводит причину ответа
#
# print("  ")
# print("Запрос окончен")



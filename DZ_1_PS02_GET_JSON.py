# Задание 1: Получение данных
# Импортируйте библиотеку requests.
# Отправьте GET-запрос к открытому API (например, https://api.github.com) с параметром для поиска репозиториев с кодом html.
# Распечатайте статус-код ответа.
# Распечатайте содержимое ответа в формате JSON.

import requests
import pprint

# создаём словарь-список того, что мы хотим получить
params = {
    'q':'language:html', # Поисковый запрос 'q' от слова query (ищем все репозитории c html)
}
# создаём переменную response в которой будем хранить ответ нашего запроса requests.get
# params(Это сам атрибут функции GET)=params(после равно, это то наш словарь созданный ранее)
response = requests.get('https://api.github.com/search/repositories', params=params)

# создаём переменную response в которой будем хранить ответ нашего запроса requests.get
response_json = response.json() #
pprint.pprint(response_json) # выводит ответ в виде словаря-списка
print("  ")

print("Ответ на основной запрос (Парсинг по ключу language:html and total_count)____________________________________________________:")
print(f"Количество репозиториев с использованием html: {response_json['total_count']}")

print("  ")
print("Статус-код ответа: ")
print(response.status_code) # выводит статус ответ - успешно или нет прошел запрос (200 -успех или 404 - не найден)
if response.ok:
   print("Ответ успешный!!!")
else:
     print("Произошла ОШИБКА - ответ не успешный^^^")
print("  ")
print("ЗАПРОС ОКОНЧЕН!___________________________________________________________________________________________!")

#Вариант НАСТАВНИКА
# import requests
#
# url = "https://api.github.com/search/repositories"
#
# params = {"q": "language:html"}
#
# response = requests.get(url, params=params)
#
# print(f"Status code: {response.status_code}")
# print(response.json())
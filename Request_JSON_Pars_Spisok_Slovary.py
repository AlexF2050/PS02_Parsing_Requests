import requests
import pprint

# создаём словарь-список того, что мы хотим получить
params = {
    'q':'python', # Поисковый запрос 'q' от слова query (ищем все репозитории c python)
}
# создаём переменную response в которой будем хранить ответ нашего запроса requests.get
# params(Это сам атрибут функции GET)=params(после равно, это то наш словарь созданный ранее)
response = requests.get('https://api.github.com/search/repositories', params=params)

# создаём переменную response в которой будем хранить ответ нашего запроса requests.get
response_json = response.json() #
pprint.pprint(response_json) # выводит ответ в виде словаря-списка
print("  ")

print("Ответ на основной запрос(Парсинг по ключу total_count)____________________________________________________:")
print(f"Количество репозиториев с использованием Python: {response_json['total_count']}")

print("  ")
print("Статус ответа: ")
print(response.status_code) # выводит статус ответ - успешно или нет прошел запрос (200 -успех или 404 - не найден)
if response.ok:
   print("Ответ успешный!!!")
else:
     print("Произошла ОШИБКА - ответ не успешный^^^")
print("  ")
print("ЗАПРОС ОКОНЧЕН!___________________________________________________________________________________________!")
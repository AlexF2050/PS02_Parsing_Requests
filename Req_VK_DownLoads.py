import requests

img = "https://sun9-7.userapi.com/impg/5edea8NPU0LYoIReQoJoMkF-xutx9Vd8_jqsiA/W6Zs9qXc6ZI.jpg?size=1080x1440&quality=95&sign=fa5517f392fa6fe1438d4733364c095c&type=album"

# отправили запрос
response= requests.get(img)

# открыть файл
with open("test.jpg", "wb") as file: #открыть файл test.jpg (создаётся автоматически open для записи и в него с помощью
       # wb будем записывать информацию из response запроса)
    file.write(response.content) # записать в файл
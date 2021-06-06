import requests

url = 'https://www.chaynikam.info/Core_i7-9700.html'
# GET -- запрос на получение данных
# POST -- отправка данных
# выполняет GET-запрос на URL
# 200 - OK (информация получена без ошибок)
# 404 - not found (информация не найдена)
# 403 - forbidden (нет прав на информацию)
# 502 - bad gateway (сервер за управляющим недоступен)

r = requests.get(url)
print(r.text)
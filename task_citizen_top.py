# Задание: найти топ-10 стран по населениюё
# name = 0
# population = 9

import json
import requests

# China - 100000000
# USA - 342000000
# ...
# Russia - 146000000
# [(10000, Country), (1460000, Russia)]

def top_10():
    url = 'https://restcountries.eu/rest/v2/all'
    r = requests.get(url)
    # [{"name": "x", "population": 11}]
    array = [(json.loads(r.text)[100]['population'], json.loads(r.text)[100]['name'])]
    array.append((146000000, 'Russia'))
    # НЕ ТРОГАТЬ, ВЫВОД ТОП-10
    array.sort(key=lambda f: -f[0])
    for num, i in enumerate(array[:10]):
        print(f'{num + 1}. {i[1]} - {i[0]}')
    # КОНЕЦ НЕ ТРОГАТЬ
    # return json.loads(r.text)

top_10()
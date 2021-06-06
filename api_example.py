import requests
import json





def get_country(name):
    # url = 'https://restcountries.eu/rest/v2/name/' + name  # очень старый и редко используется
    # url = 'https://restcountries.eu/rest/v2/name/{}'.format(name)  # используется если надо подставить 1-2 значения
    # url = 'https://restcountries.eu/rest/v2/name/{name}'.format(name=name)  # используется в python2.7+
    url = f'https://restcountries.eu/rest/v2/name/{name}'  # самый новый и используется в программах python3.5+
    r = requests.get(url)
    if r.status_code == 200:
        return json.loads(r.text)[0]
    return None


def search_country(name):
    url = f'https://restcountries.eu/rest/v2/name/{name}'
    r = requests.get(url)
    if r.status_code == 200:
        return json.loads(r.text)
    return None


search = input('Введите страну: ')
result = search_country(search)
print('Найдено стран:', len(result))
print(json.dumps(result, indent=2))

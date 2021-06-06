import json

import requests
import zipfile
from pathlib import Path

downloads = Path('downloads')
if not downloads.exists():
    downloads.mkdir()

with (downloads / 'data.zip').open('wb') as file:
    json_url = 'https://op.mos.ru/EHDWSREST/catalog/export/get?id=1111483'
    r = requests.get(json_url)
    file.write(r.content)

with zipfile.ZipFile(str(downloads / 'data.zip'), 'r') as zip_ref:
    zip_ref.extractall(str(downloads))

with (downloads / 'data-28509-2021-06-06.json').open('r', encoding='cp1251') as file:
    data = json.load(file)
    cur = data[0]
    res = f"Имя: {cur['Name']}\n" \
          f"Район: {cur['District']}\n" \
          f"Адрес: {cur['Address']}"
    print(res)

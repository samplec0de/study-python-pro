import json
with open('example.json', 'r') as file:
    json_data = json.load(file)
    print(json_data)
    print(json_data['array'])
    print(json_data['key3']['00'])
dct = {'test': [{'1': 1, '2': 2}, {'1': 1.1111, '2': 2.2222}]}
with open('example_w.json', 'w') as file:
    json.dump(dct, file, indent=2)
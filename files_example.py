# r - чтение
# w - запись (перезапись, если создан)
# a - дописывание в файл
# r+ - both read and write mode
# a+ - both read and write mode (дописывание)
# w+ - read and write mode
# b - чтение байтов

try:
    with open('dir/test1.txt', 'r') as file:
        print(file.read())
except FileNotFoundError:
    print("файл не найден")
x = int(input())
y = int(input())


class MyException(Exception):
    pass


try:
    # код, который может давать ошибку
    print(x / y)
    if x == 1 and y == 1:
        raise MyException("Вы делите 1 на 1, это ужасно!")
except ZeroDivisionError as e:
    print('нельзя делить на ноль', e)
else:
    print('all is ok')
finally:
    print('finally')
print(x + y)

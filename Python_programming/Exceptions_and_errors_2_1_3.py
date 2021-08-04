# Работа с ошибками и исключениями

def f(x, y):
    try:
        return x / y
    except TypeError:
        print('Type Error')
    except ZeroDivisionError:
        print('Zero Division Errorrrrrr')


def f(x, y):
    try:
        return x / y
    except (TypeError, ZeroDivisionError) as e:
        print('errrr', type(e), e)


def f(x, y):
    try:
        return x / y
    except:
        print('errrr')


print(f(5, 'tre'))  # None из-за того, что функция не возвращает ничего
print()
print(f(5, 0))
print()
print(f(0, 5))
print()
print(f(0, 5))

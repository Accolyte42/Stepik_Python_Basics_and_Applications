# Реализуйте программу, которая будет эмулировать работу с пространствами
# имен. Необходимо реализовать поддержку создания пространств имен и
# добавление в них переменных.
# В данной задаче у каждого пространства имен есть уникальный текстовый
# идентификатор – его имя.
# Вашей программе на вход подаются следующие запросы:
# create <namespace> <parent> –  создать новое пространство имен с именем <namespace> внутри пространства <parent>
# add <namespace> <var> – добавить в пространство <namespace> переменную <var>
# get <namespace> <var> – получить имя пространства, из которого будет взята переменная <var>
# при запросе из пространства <namespace>, или None, если такого пространства не существует

# Идея решения: создать два словаря вида {Родитель: неймспейс } и {Неймспейс: его переменные}
#
#
#

def add(namespace, var):
    # Функция добавления переменной var в пространства имен namespace
    global dct_parent, dct_variables
    dct_variables[namespace].append(var)


def create(namespace, parent):
    # Функция создания пространства имен namespace в другом parent
    global dct_parent, dct_variables
    dct_parent[namespace] = parent
    dct_variables[namespace] = []


def get(namespace, var):
    # Функция получения переменной var в пространстве имен namespace
    if var in dct_variables[namespace]:
        print(namespace)
        return namespace
    elif namespace == 'global':
        print('None')
        return 'None'
    else:
        get(dct_parent[namespace], var)


def command(cmd_in, namesp_in, arg_in):
    # Функция для применения команд по введенным переменным
    if cmd_in == 'add':
        return add(namesp_in, arg_in)
    if cmd_in == 'create':
        return create(namesp_in, arg_in)
    if cmd_in == 'get':
        return get(namesp_in, arg_in)

# Создание первых элементов
dct_parent = {'None':'global'}
dct_variables = {'global':['test']}

# add('global', 'a')
# create('foo', 'global')
# add('foo', 'b')
# get('foo', 'a')
# get('foo', 'c')
# create('bar', 'foo')
# add('bar', 'a')
# get('bar', 'a')
# get('bar', 'b')
# n  = 9

n = int(input())
for i in range(n):
    cmd, namesp, arg = input().split()
    command(cmd, namesp, arg)
   # print(cmd, namesp, arg)
   # print(dct_parent)
   # print(dct_variables)


# create('new_nmsp', 'global')
# create('new_nmsp', 'global')
# add('global', 'var11')
# add('new_nmsp', 'var22')

# add('global', 'a')
# create('foo', 'global')
# add('foo', 'b')
# create('bar', 'foo')
# add('bar', 'a')
# create('fun', 'foo')
# add('fun',)
# print(get('foo', 'a'))

# print(dct_parent)
# print(dct_variables)











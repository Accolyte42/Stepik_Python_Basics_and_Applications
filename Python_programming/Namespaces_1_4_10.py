#
#
#
#
#
#
#
# g

# Идея решения: создать два словаря вида {Родитель: неймспейс } и {Неймспейс: его переменные}
#
#
#

def add(namespace, var):
    global dct_parent, dct_variables
    dct_variables[namespace].append(var)


def create(namespace, parent):
    global dct_parent, dct_variables
    dct_parent[namespace] = parent
    dct_variables[namespace] = []


def get(namespace, var):
    if var in dct_variables[namespace]:
        print(namespace)
        return namespace
    else:
        if namespace == 'global':
            return 'None'
        get(dct_parent[namespace], var)


def command(cmd_in, namesp_in, arg_in):
    if cmd_in == 'add':
        return add(namesp_in, arg_in)
    if cmd_in == 'create':
        return create(namesp_in, arg_in)
    if cmd_in == 'get':
        return get(namesp_in, arg_in)

# Создание первых элементов
dct_parent = {'None':'global'}
dct_variables = {'global':['test']}

# n = int(input())
n  = 9
for i in range(n):
   cmd, namesp, arg = input().split()
   command(cmd, namesp, arg)
   print(cmd, namesp, arg)
   print(dct_parent)
   print(dct_variables)


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

print(dct_parent)
print(dct_variables)











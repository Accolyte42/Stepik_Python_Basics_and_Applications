

n = int(input())

# for i in range(n):
#     cmd, namesp, arg = input().split()

scopes = {'global': {'parent': None, 'variables': set()}}

def create(namespace_new, parent):
    if parent in scopes['global']:
        scopes['global'] = 123

create('nw_nspc', 'parent')

print(scopes)

def add(namespace, var):
    namespace[]













import os
import os.path
import shutil

# Функция для получения уникальных элементов списка
def get_unique(lst):
    unique = []

    for number in lst:
        if number in unique:
            continue
        else:
            unique.append(number)
    return unique


inp_dir = r'C:\Users\kolba\Desktop\main'
os.chdir(inp_dir)

lst = []

for current_dir, dirs, files in os.walk('.'):
#         print(current_dir, dirs, files)
    for fl in files:
        if fl[-3:] == '.py':
            lst.append(str('main'+current_dir[1:]))

un_lst = get_unique(lst)
un_lst.sort()

with open('output_file_2_4_6.txt', 'w') as outp:
    for l in un_lst:
        # print(l)
        outp.write(str(l)+'\n')
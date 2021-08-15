# Вам дана частичная выборка из датасета зафиксированных преступлений, совершенных в городе Чикаго с 2001 года по
# настоящее время:
# Одним из атрибутов преступления является его тип – Primary Type.
# Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.


import csv
from datetime import datetime, date, time


dict_crimes = {}
with open('Crimes.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        dt = datetime.strptime(row['Date'][:10], '%m/%d/%Y')
        if dt.year == 2015:
            try:
                dict_crimes[row['Primary Type']] += 1
            except:
                dict_crimes[row['Primary Type']] = 1

print(dict_crimes) # вывод всего списка с перступлениями и их количеством
dct_it = dict_crimes.items()
num_of_crimes = 0
most_common_crime = 'Не найдено'
for crime in dct_it:
    if crime[1] > num_of_crimes:
        num_of_crimes = crime[1]
        most_common_crime = crime[0]

print(most_common_crime, num_of_crimes)

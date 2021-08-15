# Вам дана частичная выборка из датасета зафиксированных преступлений, совершенных в городе Чикаго с 2001 года по
# настоящее время:
# Одним из атрибутов преступления является его тип – Primary Type.
# Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.





import csv
from datetime import datetime, date, time


dict_crimes = {}
with open('Crimes.csv') as f:
    reader = csv.DictReader(f)
    # print(reader.__sizeof__())
    # print(reader)
    for row in reader:
        # print(row[2][0:-3])
        # dt = row[2]
        dt = datetime.strptime(row['Date'][:10], '%m/%d/%Y')
        # print(repr(row['Date']))
        # print(repr(dt))

        # print(repr(dt.year)) # Обращение к году преступления
        # print(repr(row['Primary Type']))
        if dt.year == 2015:
            # dict_crimes[row['Primary Type']] = 1
            try:
                dict_crimes[row['Primary Type']] += 1
            except:
                dict_crimes[row['Primary Type']] = 1
        # if dt:
        #     new_dt = datetime.strptime(dt, '%m/%d/%Y %H:%M:%S %p')
        #     print(repr(datetime.strptime(dt, '%m/%d/%Y %H:%M:%S %p')))
        # print(repr(new_dt))
print(dict_crimes)


# students = [
#     ['Greg', 'Dean', 70, 80, 90, 'Good job, Greg'],
#     ['Wirt', 'Wood', 80, 80.2, 80, 'Nicely done']
# ]
#
# with open('example_csv_format', 'a') as f:
#     # writer = csv.writer(f, quoting=csv.QUOTE_ALL) # в аргументе quoting можно выбирать, что помещать в ковычки
#     writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC) # в аргументе quoting можно выбирать, что помещать в ковычки
#
#     # for student in students:
#     #     writer.writerow(student)
#     writer.writerows(students) # Данная запись экспивалентна, т.к.
#                                # интерпретатор умеет итерировать

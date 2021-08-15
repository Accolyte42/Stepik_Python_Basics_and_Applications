import csv

# with open('example_csv_format') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         if row:
#             print(row)

students = [
    ['Greg', 'Dean', 70, 80, 90, 'Good job, Greg'],
    ['Wirt', 'Wood', 80, 80.2, 80, 'Nicely done']
]

with open('example_csv_format', 'a') as f:
    # writer = csv.writer(f, quoting=csv.QUOTE_ALL) # в аргументе quoting можно выбирать, что помещать в ковычки
    writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC) # в аргументе quoting можно выбирать, что помещать в ковычки

    # for student in students:
    #     writer.writerow(student)
    writer.writerows(students) # Данная запись экспивалентна, т.к.
                               # интерпретатор умеет итерировать

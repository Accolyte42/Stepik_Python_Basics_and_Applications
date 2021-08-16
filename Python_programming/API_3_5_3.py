# В этой задаче вам необходимо воспользоваться API сайта numbersapi.com
#
# Вам дается набор чисел. Для каждого из чисел необходимо узнать, существует
# ли интересный математический факт об этом числе
#
# Для каждого числа выведите Interesting, если для числа существует интересный факт, и Boring иначе.
# Выводите информацию об интересности чисел в таком же порядке, в
# каком следуют числа во входном файле.
#
# Пример запроса к интересному числу:
# http://numbersapi.com/31/math?json=true
#
# Пример запроса к скучному числу:
# http://numbersapi.com/999/math?json=true

import requests
# city = input('City?')
# api_url = 'http://numbersapi.com/31/math?json=true'

# params = {
    # 'q': city, #'Saint Petersburg',
    # 'appid': 'fe6c9ac08e96ecdd33f559f07bc59da7',
    # 'units': 'metric'

# }
filename = 'api_1_test.txt'
# output_list = []

with open(filename) as f:
    for row in f:
        i = int(row)
        res = requests.get(f'http://numbersapi.com/{i}/math?json=true')
        data = res.json()
        if data['found']:
            print('Interesting')
        else:
            print('Boring')

        # print(data['found'])



# for i in input():
#     res = requests.get(f'http://numbersapi.com/{i}/math?json=true')
#     print(res.status_code)
#     data = res.json()
#     print(data['found'])
# template = 'Current temperature in {} is {}'
# print(template.format (city, data['main']['temp']))




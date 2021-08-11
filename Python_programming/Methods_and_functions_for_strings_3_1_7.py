
# Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.
# Выведите одно число – количество вхождений строки t в строку s.

# Пример:
# s = "abababa"
# t = "aba"

# Вхождения строки t в строку s:
# abababa
# abababa
# abababa

s = input()
t = input()

# print(str.count.__doc__)

# s = 'aaaaa'
# s = 'ff'
# t = 'a'
counter = 0
index_cur_substr = 0
while True:
    try:
        # print(counter, ' ', s[index_cur_substr:], end=' : ')
        # print(s[index_cur_substr:].index(t))
        index_cur_substr += s[index_cur_substr:].index(t)+1
        counter += 1

    except ValueError:
        # print('ValueError')
        break

print(counter)

# print(str.index.__doc__)



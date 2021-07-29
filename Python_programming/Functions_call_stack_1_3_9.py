# a = []

# def foo(arg1, arg2):
#   a.append("foo")

# foo(a.append("arg1"), a.append("arg2"))

# print(a)


# x = [1, 2, 3]
# print(x.append(4))
# print(x.append(5))

# print(x)

# top = x.pop()
# print(top)
# print(x)

# print(x.pop())
# print(top)
# print(x)

# Напишите реализацию функции closest_mod_5, принимающую в качестве
# единственного аргумента целое число x и возвращающую самое маленькое
# целое число y, такое что:
# y больше или равно x
# y делится нацело на 5
#


def closest_mod_5(x):
    while x % 5 != 0:
        x += 1
    return x

# print(closest_mod_5(-6))














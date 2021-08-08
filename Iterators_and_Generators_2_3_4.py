# Одним из самых часто используемых классов в Python является класс filter. Он
# принимает в конструкторе два аргумента a и f – последовательность и функцию,
# и позволяет проитерироваться только по таким элементам x из
# последовательности a, что f(x) равно True. Будем говорить, что в этом случае
# функция f допускает элемент x, а элемент x является допущенным.
#
# В данной задаче мы просим вас реализовать класс multifilter, который будет
# выполнять ту же функцию, что и стандартный класс filter, но будет использовать
# не одну функцию, а несколько.
#
# Решение о допуске элемента будет приниматься на основании того, сколько
# функций допускают этот элемент, и сколько не допускают. Обозначим эти количества за pos и neg.
#
# Введем понятие решающей функции – это функция, которая принимает два
# аргумента – количества pos и neg, и возвращает True, если элемент допущен, и False иначе.


class multifilter:
    def judge_half(pos, neg):
        if pos >= neg:
            return True
        else:
            return False

    def judge_all(pos, neg):
        # print('judge_all')
        if neg == 0:
            return True
        else:
            return False

    def judge_any(pos, neg):
        if pos >= 1:
            return True
        else:
            return False

    def __iter__(self):
        return self

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable
        self.judge = judge
        self.funcs = funcs
        self.index = 0
        # print('init')
        # print(self.funcs)

    def __next__(self):
        # print(len(self.iterable))
        # print()
        if self.index < len(self.iterable):
            self.index += 1
            # return self.index
            pos = 0
            neg = 0
            for f in self.funcs:
                if f(self.index-1):
                    pos += 1
                else:
                    neg += 1
            # print(self.iterable[self.index-1], self.judge(pos, neg))
            if self.judge(pos, neg):
                return self.iterable[self.index-1]
            else:
                return self.__next__()
        else:
            raise StopIteration

#             yield self.iterable[i]


def fun2(x):
    return x % 2 == 0


def fun3(x):
    return x % 3 == 0


def fun5(x):
    return x % 5 == 0


a = [i for i in range(21)]
# print(multifilter(a, fun2, fun3, fun5))
ob = multifilter(a, fun2, fun3, fun5, judge=multifilter.judge_half)
# print(ob)
# for i in
# for i in multifilter(a, fun2, fun3, fun5):
#     print(i)
    # print('TEST')

# for i in multifilter(a, fun2, fun3, fun5):
#     print(i, end=' ')
print(list(ob))





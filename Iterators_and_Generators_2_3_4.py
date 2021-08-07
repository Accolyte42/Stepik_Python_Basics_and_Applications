
class multifilter:
    def judge_half(pos, neg):
        if pos >= neg:
            return True
        else:
            return False

    def judge_all(pos, neg):
        print('judge_all')
        if neg == 0:
            return True
        else:
            return False

    def judge_any(pos, neg):
        if pos >= 1:
            return True
        else:
            return False

    def __init__(self, iterable, *funcs, judge=judge_all):
        self.iterable = iterable
        self.judge = judge
        self.funcs = funcs
        self.index = 0
        print('init')
        # print(self.funcs)

    def __iter__(self):
        return self

    def __next__(self):
        # print(len(self.iterable))
        print('next')
        if self.index < len(self.iterable):
            self.index += 1
            pos = 0
            neg = 0
            for f in self.funcs:
                if f(self.index):
                    pos += 1
                else:
                    neg += 1
            print(self.judge(pos, neg))
            if self.judge(pos, neg):
                # print(self.iterable[self.index])
                yield self.iterable[self.index]
            else:
                return self.__next__()
        raise StopIteration

#             yield self.iterable[i]


def fun2(x):
    return x % 2 == 0


def fun3(x):
    return x % 3 == 0


def fun5(x):
    return x % 5 == 0


a = [i for i in range(21)]
print(multifilter(a, fun2, fun3, fun5))
# ob = multifilter(a)
for i in multifilter(a, fun2, fun3, fun5):
    print(i)
    # print('TEST')
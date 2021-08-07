class multifilter:
    def judge_half(pos, neg):
        if pos >= neg:
            return True
        else:
            return False

    def judge_all(pos, neg):
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
        print(self.funcs[0])

    def __iter__(self):
        for i in self.iterable:
            pos = 0
            neg = 0
            # print(self.iterable[i])
            for f in self.funcs[0]:
                if f(i):
                    pos += 1
                else:
                    neg += 1
            if self.judge(pos, neg):
                yield self.iterable[i]


#             yield self.iterable[i]

def fun2(x):
    return x % 2 == 0


def fun3(x):
    return x % 3 == 0


def fun5(x):
    return x % 5 == 0


a = [i for i in range(21)]

# ob = multifilter(a)
for i in multifilter(a, fun2, fun3, fun5):
    # print(next(i))
    print(i)
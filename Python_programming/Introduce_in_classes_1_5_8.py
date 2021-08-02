# Реализуйте класс MoneyBox, для работы с виртуальной копилкой.
# Каждая копилка имеет ограниченную вместимость, которая выражается целым
# числом – количеством монет, которые можно положить в копилку. Класс
# должен поддерживать информацию о количестве монет в копилке,
# предоставлять возможность добавлять монеты в копилку и узнавать, можно ли
# добавить в копилку ещё какое-то количество монет, не превышая ее вместимость.
#
#

class MoneyBox:
    def __init__(self, capacity, count=0):
        # конструктор с аргументом – вместимость копилки
        self.capacity = capacity
        self.count = count

    def can_add(self, v):
        # True, если можно добавить v монет, False иначе
        if self.capacity - self.count >= v:
            return True
        else:
            return False

    def add(self, v):
        # положить v монет в копилку
        self.count += v

x = MoneyBox(15)
print(x.count)
if x.can_add(5): x.add(5)
print(x.count)
if x.can_add(9): x.add(9)
print(x.count)
if x.can_add(3): x.add(3)
print(x.count)

#














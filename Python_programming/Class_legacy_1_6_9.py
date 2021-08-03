# Реализуйте класс LoggableList, отнаследовав его от классов list и Loggable таким
# образом, чтобы при добавлении элемента в список посредством метода append
# в лог отправлялось сообщение, состоящее из только что добавленного элемента.

class LoggableList(list, Loggable):
    def append(self, elem):
        super().append(elem)
        return self.log(elem)













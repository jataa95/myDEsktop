from re import S


def two_digits(val):
    s = str(val)
    if len(s) == 1:
        s = '0' + s
    return s


class Timer:
    def __init__(self, h=0, m=0, s=0):
        self.__h = h
        self.__m = m
        self.__s = s

    def __str__(self):
        return two_digits(self.__h) + ':' \
            + two_digits(self.__m) + ':' + two_digits(self.__s)

    def next_sec(self):
        self.__s += 1
        if self.__s > 59:
            self.__s = 0
            self.__m += 1
            if self.__m > 59:
                self.__m = 0
                self.__h += 1
                if self.__h > 23:
                    self.__h = 0

    def prev_sec(self):
        self.__s -= 1
        if self.__s < 0:
            self.__s = 59
            self.__m -= 1
            if self.__m < 0:
                self.__m = 59
                self.__h -= 1
                if self.__h < 0:
                    self.__h = 23


timer = Timer(23, 59, 58)
print(timer)
timer.next_sec()
print(timer)
timer.prev_sec()
print(timer)

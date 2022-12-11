from random import randint


class Number:
    def __init__(self, value: str, *args, **kwargs):
        self.value = int(value)
        self.string = value
        self.__dict__.update(**kwargs)

    @property
    def color(self):
        red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
        black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
        if self.value in black:
            return 'black'
        elif self.value in red:
            return 'red'
        else:
            return 'green'

    @property
    def is_black(self):
        return self.color == 'black'

    @property
    def is_red(self):
        return self.color == 'red'

    @property
    def is_1st_12(self):
        return self.value != 0 and self.value <= 12

    @property
    def is_2nd_12(self):
        return self.value != 0 and 13 <= self.value <= 24

    @property
    def is_3rd_12(self):
        return self.value != 0 and self.value >= 25

    @property
    def is_1st_half(self):
        return self.value != 0 and self.value <= 18

    @property
    def is_2nd_half(self):
        return self.value != 0 and self.value >= 19

    def __str__(self):
        return self.string

    def __repr__(self):
        return f"Number({self.string} - {self.color})"


class Board:
    def __init__(self):
        self.numbers = [Number(str(i)) for i in range(1, 37)]
        self.numbers.append(Number('0'))
        self.numbers.append(Number('00'))


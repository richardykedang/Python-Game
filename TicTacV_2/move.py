class Move:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    def is_valid(self):
        return 1 <= self._value <= 9

    def get_row(self):
        if self._value in (1,2,3):
            return 0 # first row
        elif self._value in (4,5,6):
            return 1 # second row
        else:
            return 2

    def get_column(self):
        if self._value in (1,4,7):
            return 0 # first column
        elif self._value in (2,5,8):
            return 1 # second column
        else:
            return 2

# Testing Class Move
#           col1 col2 col3
# row 0 : | 1 | 2 | 3 |
# row 1 : | 4 | 5 | 6 |
# row 2 : | 7 | 8 | 9 |
move = Move(2)
print(move._value) # 2

print(move.is_valid()) # true

print(move.get_row()) # 0

print(move.get_column()) # 1
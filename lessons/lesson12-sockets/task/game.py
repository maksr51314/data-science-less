EMPTY_CELL = ' '


class Field:
    def __init__(self):
        self._field = [[EMPTY_CELL for _ in range(3)] for _ in range(3)]

    def __str__(self):
        return '\n'.join('|'.join(cell for cell in row) for row in self._field)

    def set_symbol(self, x, y, symbol):
        """
        >>> f = Field()
        >>> f.set_symbol(0, 0, 'X')
        >>> f._field[0][0]
        'X'
        >>> f = Field()
        >>> f.set_symbol(0, 0, 'X')
        >>> f.set_symbol(0, 0, 'X')
        Traceback (most recent call last):
        ...
        ValueError
        """
        if self._field[x][y] != EMPTY_CELL:
            raise ValueError
        self._field[x][y] = symbol

    def _test_rows(self, field):
        for row in field:
            if row[0] != EMPTY_CELL and row == [row[0]]*3:
                return True
        return False

    def _game_over_by_rows_(self):
        """
        >>> f = Field()
        >>> f._game_over_by_rows_()
        False
        >>> f = Field()
        >>> f._field[0] = ['X', 'X', 'X']
        >>> f._game_over_by_rows_()
        True
        """
        return self._test_rows(self._field)

    def _game_over_by_columns(self):
        """
        >>> f = Field()
        >>> f._game_over_by_columns()
        False
        >>> f = Field()
        >>> f._field[0][0] = ['X']
        >>> f._field[1][0] = ['X']
        >>> f._field[2][0] = ['X']
        >>> f._game_over_by_columns()
        True
        """
        field = list(zip(*self._field))
        return self._test_rows(field)

    def game_over(self):
        pass


if __name__ == '__main__':
    f = Field()
    f.set_symbol(2, 2, 'X')
    f.set_symbol(2, 1, '0')
    print(f)

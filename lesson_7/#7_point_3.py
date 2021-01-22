#point_3
class Cell:
    def __init__(self, size):
        self.size = size
        
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, value):
        if type(value) != int or value < 0:
            print('size must be a integer number that bigger than 0')
        elif type(value) == int and value >= 0:
            self._size = value
        try:
            tmp = self._size
        except AttributeError as att_err:
                self._size = 0
        return
    
    def __add__(self, b):
        if not isinstance(b, Cell):
            print('You donut! Cant add!')
            return
        return Cell(self._size + b.size)
    
    def __sub__(self, b):
        if not isinstance(b, Cell) or self._size < b.size:
            print('You donut! Cant sub!')
            return
        return Cell(self._size - b.size)
    
    def __mul__(self, b):
        if not isinstance(b, Cell):
            print('You donut! Cant multiply!')
            return
        return Cell(self._size * b.size)
    
    def __truediv__(self, b):
        if not isinstance(b, Cell) or b.size == 0:
            print('You donut! Cant div!')
            return
        return Cell(self._size//b.size)
    
    def make_order(self, n):
        if type(n) == int and n>0:
            int_rows = self._size//n
            res_rows = self._size%n
            return ('*'*n + '\n')*int_rows + '*'*res_rows if res_rows != 0 else (('*'*n + '\n')*int_rows)[:-1]
        else:
            print('You donut! Cand order!')
            return
        
        
cell_1 = Cell(10)
cell_2 = Cell(20)
print((cell_1 + cell_2).size)
print((cell_2 - cell_1).size)
cell_1 - cell_2
print((cell_1*cell_2).make_order(10) + '\n')

cell_3 = Cell(12)
print(cell_3.make_order(5) + '\n')
cell_4 = Cell(15)
print(cell_4.make_order(5) + '\n')
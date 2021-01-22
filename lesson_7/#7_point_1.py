"""
1. Как сделать так, чтобы к матрицам можно было обращаться через индексы, а не с помощью специльного метода?
    Понимаю, что надо перегрузить какой-то метод, но не могу найти какой :(
"""
#point_1
class Matrix:
    def __init__(self, input_data):
        """Находим самую длинный список во входных данных, чтобы
           если в каких-то списках не хватает чисел — добить нулями"""
        list_of_len = list(map(len, input_data))
        max_len = max(list_of_len)
        self.matrix = []
        self.rows = len(input_data)
        self.cols = max_len
        for i in range(self.rows):
            self.matrix.append([0]*max_len)
            for j in range(list_of_len[i]):
                try:
                    self.matrix[i][j] = float(input_data[i][j])
                except ValueError as val_err:
                    print(str(val_err) + '\n' + 'init was failed!')
                    del self.matrix
                    return
        return
    
    def get_el(self, row, col):
        return self.matrix[row][col]
    
    def set_el(self, row, col, el):
        self.matrix[row][col] = el
        return
    
    def __str__(self):
        matrix_to_print = ''
        for i in range(self.rows):
            matrix_to_print += str(self.matrix[i])[1:len(str(self.matrix[i]))-1].replace(',', '') + '\n'
        return matrix_to_print
        
    def __add__(self, b):
        if not isinstance(b, Matrix):
            print('You donut! Cant add!')
            return
        elif self.rows != b.rows or self.cols != b.cols:
            print('You donut! Cant add matrices with different dimensions!')
            return
        result_matrix = Matrix([[0]*self.cols]*self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                result_matrix.set_el(i, j, self.matrix[i][j] + b.get_el(i,j))
        return result_matrix
        
        
    
matrix_1 = Matrix([[1,2,3], [3,4,5], [8,9,10,11,12]])
matrix_2 = Matrix([[1,2,3], [3,4,5], [13,14,15,16,17]])
matrix_3 = Matrix([[1,2,3], [1,2,3]])
matrix_1 + matrix_3
print()
print(str(matrix_1 + matrix_2))

#point_5
class ComplexNumber():
    def __init__(self, real, imag = 0):
        self._real = ComplexNumber.is_correct_for_complex(real)
        self._imag = ComplexNumber.is_correct_for_complex(imag)
        
    def get_real(self):
        return self._real
    
    def get_imag(self):
        return self._imag
    
    @staticmethod
    def is_correct_for_complex(el):
        try:
            tmp_1 = complex(el)
            if tmp_1.imag != 0:
                print('That obj cant be a part of complex number, because this is already complex')
                return 0
        except ValueError:
            print('That obj cant be a part of complex number, because this is a non number type')
            return 0
        tmp_2 = float(el)
        tmp_3 = int(tmp_2)
        return tmp_3 if tmp_2 - tmp_3 == 0 else tmp_2
        
    def __add__(self, other):        
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self._real + other.get_real(), self._imag + other.get_imag())
        elif type(other) == complex:
            return ComplexNumber(self._real + other.real, self._imag + other.imag)
        elif type(other) == float or type(other) == int:
            return ComplexNumber(self._real + other, self._imag)
        else:
            print('cant add that obj!')
            return 0
    
    def __mul__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self._real*other.get_real() - self._imag*other.get_imag(), self._real*other.get_imag() + self._imag*other.get_real())
        elif type(other) == complex:
            return ComplexNumber(self._real*other.real - self._imag*other.imag, self._real*other.imag + self._imag*other.real)
        elif type(other) == float or type(other) == int:
            return ComplexNumber(self._real*other, self._imag*other)
        else:
            print('cant mult that obj!')
            return 0
    
    def __str__(self):
        return str(self._real) + '+' + str(self._imag)+ 'j' if self._imag >= 0 else str(self._real) + str(abs(self._imag)) + 'j'
    
#test
complex_1 = ComplexNumber(1, 3)
complex_2 = ComplexNumber(2, -1)
col_1 = 1+3j
col_2 = 2-1j
complex_3 = complex_1 + complex_2
complex_4 = complex_1 * complex_2
complex_5 = complex_1 * 10
complex_6 = complex_1 * 0.5
print(col_1 + col_2)
print(col_1 * col_2)
print(col_1 * 10)
print(col_1 * 0.5)
print(str(complex_3))
print(str(complex_4))
print(str(complex_5))
print(str(complex_6))
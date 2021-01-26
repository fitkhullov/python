#point_3
class MyException(Exception):
    def __init__(self, text):
        self.text = text
        
    @staticmethod
    def check(el):
        print(el)
        try:
            tmp_1 = complex(el)
            if tmp_1.imag != 0:
                return tmp_1
        except ValueError:
            raise MyException('you cant add type that is not a number')
        tmp_2 = float(el)
        tmp_3 = int(el)
        return tmp_2 if tmp_2 - tmp_3 == 0 else tmp_3

spec = 'stop'
x = [] #список с числами
while True:
    tmp = input('enter a number: ')
    if tmp == spec:
        break
    try:
        x.append(MyException.check(tmp))
    except MyException as my_excp:
        print(my_excp.text)

print(x)
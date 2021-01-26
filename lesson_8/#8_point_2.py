#point_2
class MyException(Exception):
    def __init__(self, text_err = 'Donut!'):
        self.text_err = text_err

while True:
    try:
        el = float(input('enter a number: '))
        try:           
            if el == 0:
                raise MyException('cannot be divided by zero')
        except MyException as excp:
            print('Donut!'+excp.text_err)
    except ValueError as val_err:
        print('donut! enter a NUMBER!')
    if input('wanna stop? type yes, dude, im tired: ').lower() == 'yes':
        break
    
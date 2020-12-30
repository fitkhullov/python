#point_1
def div(a, b):
    try:
        a/b
    except ZeroDivisionError:
        print('Деление на ноль!')
        return False
    return a/b


a, b = input().split()
print(div(int(a), int(b)))
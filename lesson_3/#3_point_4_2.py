#point_4_2
def my_func(x,y):
    first = x
    while y < -1:
        x *= first
        y += 1
    return 1/x


x, y = [int(i) for i in input().split()]
print(my_func(x,y))
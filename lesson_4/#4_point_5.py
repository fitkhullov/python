#point_5
from functools import reduce

def reduce_mult(a, b):
    return a*b


start_list = [i for i in range(100, 105, 2)]
print(reduce(reduce_mult, start_list))

#point_6_2
from system import argv
from itertools import cycle

script_name, num_end = argv
input_list = '1 2 3 4 5 6 7'
for el in cycle(input_list):
    if num_end == 0:
        break
    print(el)    
    num_end -= 1


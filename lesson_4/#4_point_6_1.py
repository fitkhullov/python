#point_6_1
from system import argv
from itertools import count

script_name, num_start = argv
for iterator in count(num_start, 1):
    if iterator >= num_start + 10:
        break
    print(iterator)

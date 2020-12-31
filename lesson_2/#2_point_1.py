#point_1
Q = [1, 1.0, 5+4j, '', [], ('a', 1), {1,2,3}, {}, False, None]
for var in Q:
    print(type(var))
try:
    c = 1/0
except ZeroDivisionError as err:
    print(type(err))
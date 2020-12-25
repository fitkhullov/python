#point_3
def my_func(x, y, z):
    if 0 in [x, y, z]:
        return sum([x,y,z])       
    return x+y if x>z and y>z else x+z if x>y and z>y else y+z


x, y, z = input().split()
print(my_func(int(x), int(y), int(z)))
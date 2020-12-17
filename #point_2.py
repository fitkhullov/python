#point_2
t = int(input())
h = t//3600
m = (t - h*3600)//60
s = (t - h*3600 - m*60)
if (h>9 and m>9 and s>9):
    print(h,m,s, sep=':')
elif (h<9 and m>9 and s>9):
    print(f'0{h}:{m}:{s}')
elif (h<9 and m<9 and s>9):
    print(f'0{h}:0{m}:{s}')
elif (h<9 and m<9 and s< 9):
    print(f'0{h}:0{m}:0{s}')
elif (h>9 and m<9 and s>9):
    print(f'{h}:0{m}:{s}')
elif (h>9 and m<9 and s<9):
    print(f'{h}:0{m}:0{s}')
elif (h>9 and m>9 and s<9):
    print(f'{h}:{m}:0{s}')
else:
    print(f'0{h}:{m}:0{s}')
#point_2
t = int(input())
h = t//3600
m = (t - h*3600)//60
s = (t - h*3600 - m*60)
h = '0'+str(h) if h<10 else h
m = '0'+str(m) if m<10 else m
s = '0'+str(s) if s<10 else s
print(h,m,s, sep = ':')
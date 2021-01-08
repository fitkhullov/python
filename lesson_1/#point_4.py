#point_4
N = input()
l = len(N)
N = int(N)
f_dig = N//10**(l-1)
s_dig = (N - f_dig*10**(l-1))//10**(l-2)
max_dig = s_dig if f_dig < s_dig else f_dig
while (l>0):    
    N -= (f_dig*10**(l-1) + s_dig*10**(l-2))
    l -= 2
    f_dig = N//10**(l-1)
    s_dig = (N - f_dig*10**(l-1))//10**(l-2)
    curr_max = s_dig if f_dig < s_dig else f_dig
    max_dig = curr_max if max_dig < curr_max else max_dig    
print(max_dig)
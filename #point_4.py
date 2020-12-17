#point_4
N = input()
l = len(N)
N = int(N)
f_dig = N//10**(l-1)
s_dig = (N - f_dig*10**(l-1))//10**(l-2)
if (f_dig < s_dig): max_dig = s_dig
else: max_dig = f_dig
while (l>0):    
    N -= (f_dig*10**(l-1) + s_dig*10**(l-2))
    l -= 2
    f_dig = N//10**(l-1)
    s_dig = (N - f_dig*10**(l-1))//10**(l-2)
    if (f_dig < s_dig): curr_max_dig = s_dig
    else: curr_max_dig = f_dig
    if (max_dig < curr_max_dig):
        max_dig = curr_max_dig
print(max_dig)
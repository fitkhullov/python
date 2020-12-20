#point_2
n = int(input('Введите кол-во эл-ов в списке: '))
L = [i+1 for i in range(n)]
if n//2 == 0:
    for i in range(0,n,2):
        L[i], L[i+1] = L[i+1], L[i]
else:
    for i in range(0, n-1, 2):
        L[i], L[i+1] = L[i+1], L[i]
print(L)
#point_7
def fact(n):
    el = 1
    for i in range(1, n+1):
        yield el
        el *= (i+1)

n = int(input())
for pos, num in enumerate(fact(n)):
    print(f'{pos+1}. {num}')
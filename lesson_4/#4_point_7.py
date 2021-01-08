#point_7
def fact(n):
    gen_of_fact = 1
    for increaser in range(1, n+1):
        yield gen_of_fact
        gen_of_fact *= (increaser+1)

n = int(input())
for pos, num in enumerate(fact(n)):
    print(f'{pos+1}. {num}')

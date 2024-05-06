def fatorial(n):
    fat = 1
    for i in range(1, n + 1):
        fat *= i
    return fat

while True:
    try:
        M, N = map(int, input().split())
        print(fatorial(M) + fatorial(N))
    except:
        break

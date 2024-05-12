N = int(input())
distancia_total = 0
for _ in range(N):
    T, V = map(int, input().split())
    distancia_total += T * V
print(distancia_total)

import math

N = int(input())

for _ in range(N):
    F1, F2 = map(int, input().split())  # Quantidade de figurinhas que Ricardo e Vicente têm para trocar
    print(math.gcd(F1, F2))  # Imprime o tamanho máximo da pilha de figurinhas que poderia ser trocada

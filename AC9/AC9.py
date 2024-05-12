"""
exercicio: 1016

"""

n=int(input())
print("{} minutos".format(n*2))

"""
exercicio: 1153
"""

n=int(input())
s=1
for i in range(n,1,-1):
    s = s*i
print(s)

"""
exercicio: 1281
"""

N = int(input())
for _ in range(N):
    M = int(input())
    precos = {}
    for _ in range(M):
        produto, preco = input().split()
        precos[produto] = float(preco)
    P = int(input())
    total = 0
    for _ in range(P):
        produto, quantidade = input().split()
        total += precos[produto] * int(quantidade)
    print('R$ {:.2f}'.format(total))


"""
exercicio: 2006
"""

T = int(input())
respostas = list(map(int, input().split()))

corretas = respostas.count(T)

print(corretas)

"""
exercicio: 2339
"""

a, b, c = input().split()
if(int(a) * int(c) <= int(b)):
    print('S')
else:
    print('N')

"""
exercicio: 2388
"""

N = int(input())
distancia_total = 0
for _ in range(N):
    T, V = map(int, input().split())
    distancia_total += T * V
print(distancia_total)

"""
exercicio: 2413
"""

t = int(input())
t = t * 2 * 2
print(t)

"""
exercicio: 3048
"""

lista = []

for _ in range(int(input())):
    numero = input()
    if not lista:
        lista.append(numero)
    elif numero != lista[-1]:
        lista.append(numero)

print(len(lista))
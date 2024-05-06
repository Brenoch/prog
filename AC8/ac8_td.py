"""
- AC8 -
Exercício : 1028

"""
import math

N = int(input())

for _ in range(N):
    F1, F2 = map(int, input().split())  # Quantidade de figurinhas que Ricardo e Vicente têm para trocar
    print(math.gcd(F1, F2))  # Imprime o tamanho máximo da pilha de figurinhas que poderia ser trocada

"""
Exercicío : 1161
"""

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

"""
Exercicio: 1170
"""
N = int(input()) # Número de casos de teste
for _ in range(N):
    C = float(input())  # Quantidade de comida disponível para Blobs
    dias = 0  # Contador de dias
    while C > 1:  # Enquanto a comida for maior que 1 kg
        C /= 2  # Blobs come metade da comida
        dias += 1  # Passa um dia
    print(f'{dias} dias')  # Imprime o número de dias

"""
Exercicio: 1171
"""
N = int(input())  # Número de valores que serão lidos
valores = [int(input()) for _ in range(N)]

contador = {valor: valores.count(valor) for valor in set(valores)}

for valor in sorted(contador):
    print(f'{valor} aparece {contador[valor]} vez(es)')

"""
Exercicio: 1329
"""
while True:
    n = int(input())
    if n == 0:
        break

    resultados= list(map(int, input().split()))

    vitorias_joao = resultados.count(1)
    vitorias_maria = resultados.count(0)

    print(f"Mary won {vitorias_maria} times and John won {vitorias_joao} times")

"""
Exercicio: 1555
"""

N = int(input())
for _ in range(N):
    # O prograna está pedindo ao usuário para inserir dois números separados por um espaço.
    x, y = map(int, input().split())
    a = (3*x)**2 + y**2
    b = 2*(x**2) + (5*y)**2
    c = -100*x + y**3
    resultados = {'Rafael': a, 'Beto': b, 'Carlos': c}
    # A função max está sendo usada para encontrar a chave no dicionário resultados que tem o maior valor.
    vencedor = max(resultados, key=resultados.get)
    print(f'{vencedor} ganhou')

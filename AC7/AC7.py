"""
- AC7 -
Exercício : 1048

"""
def aumento_salario():
    salario = float(input())
    if salario <= 400:
        reajuste = 15
    elif salario <= 800:
        reajuste = 12
    elif salario <= 1200:
        reajuste = 10
    elif salario <= 2000:
        reajuste = 7
    else:
        reajuste = 4

    novo_salario = salario + (salario * reajuste / 100)
    print(f'novo salario: {novo_salario:.2f}')
    print(f'reajuste ganho: {novo_salario - salario:.2f}')
    print(f'em percentual:. {reajuste:}%')


aumento_salario()

"""
Exercício : 1065

"""
def pares_entre_cinco_numeros(num):
    if num % 2 == 0 :
        return True
    return False

def main():
    pares = 0
    for i in range(5):
        num = int(input())
        if pares_entre_cinco_numeros(num):
            pares += 1
    print(f"{pares} valores pares")

main()

"""
Exercício : 1132

"""
def nao_multiplos_de_13 (x, y):
    soma = 0
    if x > y:
        x, y = y, x

    for num in range(x, y + 1):
        if num % 13 != 0:
            soma += num
    return soma

x = int(input())
y = int(input())

print(nao_multiplos_de_13(x, y))

"""
exercício : 1173

"""
def prenchimento_vetor():
    n = int(input())

    vetor = [0] * 10
    vetor[0] = n

    for i in range(1, 10):
        vetor[i] = vetor[i - 1] * 2

    for i in range(10):
        print(f"N[{i}] = {vetor[i]}")

prenchimento_vetor()

"""
Exercício : 1180

"""
def menor_e_posicao():
    N = int(input())
    # A função map() é usada para converter cada item da lista em um inteiro.
    X = list(map(int, input().split()))

    menor_valor = min(X)
    posicao = X.index(menor_valor)

    print("Menor valor:", menor_valor)
    print("Posicao:", posicao)

menor_e_posicao()



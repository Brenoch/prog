"""----------------------------EX.1000------------------------------------------"""

print("Ola Mundo")

"""----------------------------Fim EX.1000----------------------------------------"""

"""----------------------------EX.1001----------------------------------------"""
dados1= input()
dados2= input()

dados1 = dados1.split("-")
dados2 = dados2.split("-")

preco = int(dados1[1]) * float(dados1[2]) + int(dados2[1]) * float(dados2[2])
print(f"VALOR A PAGAR: R$ {preco:.2f}")

"""----------------------------Fim EX.1001----------------------------------------"""

"""----------------------------EX.1010----------------------------------------"""

A = round(float(input()))
B = round(float(input()))
X = A + B


print(f"X = {X}")

"""----------------------------FIM EX.1010----------------------------------------"""

"""----------------------------EX.1013----------------------------------------"""

numeros = input().split()

a = int(numeros[0])
b = int(numeros[1])
c = int(numeros[2])

maior = max(a, b, c)
print(f"{maior} eh o maior")

"""----------------------------FIM EX.1013----------------------------------------"""


"""----------------------------EX.1015----------------------------------------"""

"""----------------------------FIM EX.1015----------------------------------------"""
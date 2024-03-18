"""----------------------------EX.1----------------------------------------"""
def determina_tipo_triangulo(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "Não é um triângulo"

    elif a == b == c:               #Todos os lados iguais
        return "Equilátero"

    elif a == b or a == c or b == c:
        return "Isósceles"           #  Dois lados iguais
    else:
        return "Escaleno"            #  Nenhum dos lados são iguais

def testa_triangulo():
    print(determina_tipo_triangulo(4, 4, 4)) # Equilátero
    print(determina_tipo_triangulo(2, 4, 4)) # Isósceles
    print(determina_tipo_triangulo(3, 4, 5)) # Escaleno
    print(determina_tipo_triangulo(1, 1, 4)) # Não é um triângulo
testa_triangulo()

"""--------------------------FIM EX.1--------------------------------"""


"""---------------------------EX.2-------------------------------------"""

def dia_semana(dia):
    if  dia == 1:
        return "Domingo"
    elif  dia == 2:
        return "Segunda-feira"
    elif dia == 3:
          return "Terça-Feira"
    elif  dia == 4:
        return "Quarta-feira"
    elif dia == 5:
          return "Quinta-Feira"
    elif  dia == 6:
        return "Sexta-feira"
    elif dia == 7:
          return "Sábado"
    return "Dia Inválido"


def testa_dia_semana():
    print(dia_semana(2)) # segunda-feira
    print(dia_semana(6)) # sexta-feira
    print(dia_semana(7)) # sábado
    print(dia_semana(8)) # string vazia

testa_dia_semana()

"""--------------------------FIM EX.2--------------------------------"""



"""---------------------------EX.3-------------------------------------"""
def calculadora(operador, a, b):
    if operador == '+':
        return a + b
    elif operador == '-':
        return a - b
    elif operador == '*':
        return a * b
    elif operador == 'divisão':
        if b != 0:
            return a / b
        else:
            return "Erro: Divisão por zero"
    return "Operação Inválida"


a = input("Informe o primeiro número: ")
b = input("Informe o segundo número: ")
opr1 = input("Informe a operação (+, - , *, /): ")


resultado = calculadora(opr1, float(a), float(b))
print(f"Resultado: {resultado:}")
"""--------------------------FIM EX.3--------------------------------"""



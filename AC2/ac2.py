"""
Programação Estruturada
2024.1
10/03/2024

AC2
"""
def eq_seg_grau(a, b, c):
    delta = b ** 2 - 4 * a * c
    x1 = (-b + (delta ** 0.5)) / (2 * a)
    x2 = (-b - (delta ** 0.5)) / (2 * a)
    return f"{a}x² + {b}x + {c} = 0 tem raízes: x1 = {x1}, x2 = {x2}"

# Solicita os valores dos coeficientes da equação ao usuário
A = float(input("Informe o parâmetro a da equação: "))
B = float(input("Informe o parâmetro b da equação: "))
C = float(input("Informe o parâmetro c da equação: "))

# Chama a função para calcular as raízes e imprime o resultado
print(eq_seg_grau(A, B, C))


###########################################################################
#                          bissexto                           #
###########################################################################

def eh_bissexto(ano):
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

ano = int(input('Ano:'))
resultado = eh_bissexto(ano)

print(resultado)


###########################################################################
#                          calcular salario                           #
###########################################################################

def calcula_salario(valor_hora, num_horas, irpf=0.275 ):
    salario_bruto = valor_hora * num_horas
    salario_liquido = salario_bruto * (1 - irpf)
    return salario_liquido

valor_por_hora = float(input("Informa o valor do salário por hora:" ))
hora_trabalhadas = float(input("Informe o número de horas trabalhadas no mês:"))

salario_liquido =  calcula_salario(valor_por_hora, hora_trabalhadas )
print ("O seu salário líquido é R$", salario_liquido)

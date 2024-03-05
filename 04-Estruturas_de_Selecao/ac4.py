"""
Programação Estruturada
2024.1
05/03/2024

AC4
"""

def ler_nome_usuario():

    return input("Informe o seu nome: ")

def ler_notas():
    """
    Lê e retorna quatro notas do tipo float.
    """
    n1 = float(input("Informe sua ap1:"))
    n2 = float(input("Informe sua ap2:"))
    asub = float(input("Informe sua as:"))
    ac = float(input("Informe sua ac:"))
    return n1, n2, asub, ac

def validar_notas(ap1, ap2, asub, ac):
    """
    Retorna False se pelo menos uma das notas for menor que zero ou
    maior que dez.
    """
    if ap1 > 10 or ap1 < 0:
        return False

    if ap2 > 10 or ap2 < 0:
        return False

    if asub > 10 or asub < 0:
        return False

    if ac > 10 or ac < 0:
        return False
    return True

def duas_maiores_notas(ap1, ap2, asub):
    """
    Retorna as duas maiores notas dentre as informadas.
    """
    if  asub > ap1:
        return asub, ap2

    if asub > ap2:
        return ap1, asub
    return ap1, ap2


def calcular_media(n1, n2, ac):
    """
    Calcula e retorna a média do usuário.
    """
    return (n1 + n2) * 0.4 + ac * 0.2

def informar_aprovacao(media):
    """
    Informa se o aluno passou ou não na disciplina.
    """
    print("Sua média foi", round(media, 2))
    if media >= 7:
        print("Parabéns, você foi aprovado!")
    else:
        print("Você foi reprovado...")

def main():
    nome = ler_nome_usuario()
    if nome:
        ap1, ap2, asub, ac = ler_notas()
        if validar_notas(ap1, ap2, asub, ac):
            n1, n2 = duas_maiores_notas(ap1, ap2, asub)
            media = calcular_media(ap1, ap2, ac)
            informar_aprovacao(media)

main()
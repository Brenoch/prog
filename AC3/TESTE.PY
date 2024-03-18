def dia_semana(dia):
    if  dia == 7:
        return "Domingo"
    elif  dia == 1:
        return "Segunda-feira"
    elif dia == 2:
          return "Terça-Feira"
    elif  dia == 3:
        return "Quarta-feira"
    elif dia == 4:
          return "Quinta-Feira"
    elif  dia == 5:
        return "Sexta-feira"
    elif dia == 6:
          return "Sábado"
    return "Dia Inválido"


def testa_dia_semana():
    print(dia_semana(2)) # segunda-feira
    print(dia_semana(6)) # sexta-feira
    print(dia_semana(7)) # sábado
    print(dia_semana(9)) # string vazia

testa_dia_semana()
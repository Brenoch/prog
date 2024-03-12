"""
    Programação Estuturada
    2024.1
    12/03/2024

    """

import random

def main():
    vida_aventureiro= 100
    ataque_aventureiro = random.randint(10, 20)
    defesa_aventureiro = random.randint(1, 5)
    vida_monstro = random.randint(60, 80)
    ataque_monstro = random.randint(20, 30)

#Definição dos atributos

    print("Atributos do Aventureiro")
    print(f"vida : {vida_aventureiro} ")
    print(f"ataque : {ataque_aventureiro}")
    print(f"defesa : {defesa_aventureiro}")
    print("\nAtributos do monstro")
    print(f"vida : {vida_monstro}")
    print(f"ataque : {ataque_monstro}")

    rodada = 1

    while vida_aventureiro > 0 and vida_monstro > 0:
        print(f"\nrodada {rodada}:")

        print(f"Aventureiro: vida {vida_aventureiro} - att {ataque_aventureiro} - def {defesa_aventureiro}")
        print(f"Monstro: vida {vida_monstro} - att {ataque_monstro}")


        #ataque aventureiro
        dano_av = random.randint(1, ataque_aventureiro)

        vida_monstro -= ataque_aventureiro
        print(f"O aventureiro atacou o monstro e deu {dano_av} de dano")

        # verificar se o monstro morreu
        if vida_monstro <= 0:
            print("Monstro Morreu")
            break

        #ataque monstro
        dano_monstro = random.randint(1, ataque_monstro) - defesa_aventureiro
        vida_aventureiro -= dano_monstro
        print(f"O monstro atacou o aventureiro e deu {dano_monstro} de dano")

        if vida_aventureiro <= 0:
            print("Aventureiro Morreu")
            break

        rodada += 1

main()

from collections import Counter

def calcular_porcentagem(lista_arvores):
    contador_arvores = Counter(lista_arvores)
    total_arvores = len(lista_arvores)
    porcentagens_arvores = {arvore: (contagem / total_arvores) * 100 for arvore, contagem in contador_arvores.items()}
    return porcentagens_arvores

def imprimir_porcentagens_arvores(porcentagens_arvores):
    for arvore in sorted(porcentagens_arvores.keys()):
        print(f"{arvore} {porcentagens_arvores[arvore]:.4f}")

N = int(input())

for _ in range(N):
    lista_arvores = []
    while True:
        arvore = input()
        if arvore == '':
            break
        lista_arvores.append(arvore)
    porcentagens_arvores = calcular_porcentagem(lista_arvores)
    imprimir_porcentagens_arvores(porcentagens_arvores)
    if _ < N-1:
        print()

from collections import defaultdict

def calcular_porcentagem_arvores():
    N = int(input())
    input()

    for _ in range(N):
        contagem_arvores = defaultdict(int)
        total_arvores = 0

        while True:
            try:
                arvore = input()
                if arvore == '':
                    break
                contagem_arvores[arvore] += 1
                total_arvores += 1
            except EOFError:
                break

        porcentagens = {arvore: (contagem / total_arvores) * 100 for arvore, contagem in contagem_arvores.items()}

        for arvore in sorted(porcentagens.keys()):
            print(f'{arvore} {porcentagens[arvore]:.4f}')

        if _ < N - 1:
            print()

calcular_porcentagem_arvores()

while True:
    n = int(input())
    if n == 0:
        break

    resultados= list(map(int, input().split()))

    vitorias_joao = resultados.count(1)
    vitorias_maria = resultados.count(0)

    print(f"Mary won {vitorias_maria} times and John won {vitorias_joao} times")
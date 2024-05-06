N = int(input())
for _ in range(N):
    # O prograna está pedindo ao usuário para inserir dois números separados por um espaço.
    x, y = map(int, input().split())
    a = (3*x)**2 + y**2
    b = 2*(x**2) + (5*y)**2
    c = -100*x + y**3
    resultados = {'Rafael': a, 'Beto': b, 'Carlos': c}
    # A função max está sendo usada para encontrar a chave no dicionário resultados que tem o maior valor.
    vencedor = max(resultados, key=resultados.get)
    print(f'{vencedor} ganhou')
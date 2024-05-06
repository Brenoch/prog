N = int(input())  # Número de valores que serão lidos
valores = [int(input()) for _ in range(N)]

contador = {valor: valores.count(valor) for valor in set(valores)}

for valor in sorted(contador):
    print(f'{valor} aparece {contador[valor]} vez(es)')

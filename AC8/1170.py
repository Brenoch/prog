N = int(input()) # Número de casos de teste
for _ in range(N):
    C = float(input())  # Quantidade de comida disponível para Blobs
    dias = 0  # Contador de dias
    while C > 1:  # Enquanto a comida for maior que 1 kg
        C /= 2  # Blobs come metade da comida
        dias += 1  # Passa um dia
    print(f'{dias} dias')  # Imprime o número de dias

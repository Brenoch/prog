lista = []

for _ in range(int(input())):
    numero = input()
    if not lista:
        lista.append(numero)
    elif numero != lista[-1]:
        lista.append(numero)

print(len(lista))
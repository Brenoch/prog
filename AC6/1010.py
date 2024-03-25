dados1= input()
dados2= input()

dados1 = dados1.split()
dados2 = dados2.split()

preco = int(dados1[1]) * float(dados1[2]) + int(dados2[1]) * float(dados2[2])
print(f"VALOR A PAGAR: R$ {preco:.2f}")
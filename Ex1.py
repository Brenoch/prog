
A = float(input("Informe o parâmetro a da equação: "))
B = float(input("Informe o parâmetro b da equação: "))
C = float(input("Informe o parâmetro c da equação: "))

delta = B ** 2 - 4 * A * C
x1 = (- B + delta**0.5)/(2*A)
x2 = (- B - delta**0.5)/(2*A)

print(x1)
print(x2)


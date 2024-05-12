N = int(input())
for _ in range(N):
    M = int(input())
    precos = {}
    for _ in range(M):
        produto, preco = input().split()
        precos[produto] = float(preco)
    P = int(input())
    total = 0
    for _ in range(P):
        produto, quantidade = input().split()
        total += precos[produto] * int(quantidade)
    print('R$ {:.2f}'.format(total))

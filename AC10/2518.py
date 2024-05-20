import math
while True:
    try:
        n = int(input())
        h, c, l = input().split()

        hip = math.sqrt((int(c)**2)+(int(h)**2))
        hip *= (int(l)/100*int(n))/100
        print('%.4f'%hip)

    except EOFError:
        break
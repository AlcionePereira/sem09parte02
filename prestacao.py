par = 0
pres = 0
casa = float(input())
for c in range(1, 25, 1):
    par = par + 1
    pres = (casa / c)
    print( f'{par}x de R$ {pres:.2f}' )

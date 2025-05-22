niveles = 3  

for i in range(1, niveles + 1):
    estrellas = '*' * (2 * i - 1)
    print(estrellas.center(2 * niveles - 1))
print('I'.center(2 * niveles - 1))

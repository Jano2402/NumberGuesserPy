import math
mayomen = int(input('Tú número es mayor o menor a 50, 1 = mayor, 2 = menor, 3 = igual: '))

contador = 1
intento = 0

def mayor(num):
    global contador
    global intento
    mitad = 50/(2**contador)
    contador += 1
    intento += 1
    numact = num + mitad
    if numact > 99.5: 
        numactint = math.ceil(numact)
    else:
        numactint = int(numact)
    mayomenMay = (int(input(f'Tu número es mayor o menor a {numactint}, 1 = mayor, 2 = menor, 3 = igual: ')))
    if mayomenMay == 1:
        mayor(numact)
    elif mayomenMay == 2:
        menor(numact)
    else:
        print(f'Lo adiviné en {intento} intentos')


def menor(num):
    global contador
    global intento
    mitad = 50/(2**contador)
    contador += 1
    intento += 1
    numact = num - mitad
    numactint = int(numact)
    mayomenMen = (int(input(f'Tu número es mayor o menor a {numactint}, 1 = mayor, 2 = menor, 3 = igual: ')))
    if mayomenMen == 1:
        mayor(numact)
    elif mayomenMen == 2:
        menor(numact)
    else:
        print(f'Lo adiviné en {intento} intentos')

if mayomen == 1:
    mayor(50)
elif mayomen == 2:
    menor(50)
else:
    print('Tú numero es el 50')
from email.mime import base


def potencia():
    LIMITE = 1000 #Constante se define en mayus
    contador = 0
    pot_2 = 2**contador
    while pot_2 < LIMITE:
        print('2 elevado a' + str(contador) + 'es igual a: ' + str(pot_2))
        contador += 1
        pot_2 = 2**contador


if __name__ == '__main__':
    potencia()
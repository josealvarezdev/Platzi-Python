import random

def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input('Elegi un numero del 1 al 100: '))
    vidas = 5
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print('Busca un numero mas grande')
            vidas -= 1
        else:
            print('Busca un numero mas chico')
            vidas -= 1
        if vidas == 0 and numero_elegido != numero_aleatorio:
            print ('GAME OVER')
            break
        print_vidas = str(vidas)
        print ('Te quedan ' + print_vidas + ' vidas')
        numero_elegido = int(input('Escoge otro numero: '))
    if numero_elegido == numero_aleatorio:
        print ("GANASTE!")


if __name__ == '__main__':
    run()
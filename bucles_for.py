# def while_t1:
#     contador = 1
#     while (contador < 1000):
#         contador += 1
#         print("Contador: ", contador)
# Esto en for son 2 lineas

def run():
    for contador in range(1, 1001):
        print ("Contador en for: ", contador)
        
    for i in range(1, 10):
        print (11*i)


def string():
    frase = input('Escribe una frase')
    for caracter in frase:
        print (caracter.upper())


if __name__ == "__main__":
    string()
def run():
    poblacion_paises = {
        "Argentina": 44938712,
        "Bolivia": 11510225,
        "Brasil": 210147125,
        "Colombia": 50372424,
    }
    for pais, poblacion in poblacion_paises.items():
        print(pais + ' tiene ' + str(poblacion) + ' habitantes')

if __name__ == "__main__":
    run()
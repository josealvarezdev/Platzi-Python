# menu = """
# CC2022 - CoinConversor 💰
# 1- ARP (Argentine pesos)
# 2- UYU (Uruguayan pesos)
# 3- CLP (Chilean peso)

# Choose one option:"""

# option = int(input(menu))

# if option == 1:
#     coin = input("How many argentinian pesos do you have?")
#     coin = float(coin)

#     dolar_value = 3000
#     dollar_convertion = coin / dolar_value
#     dollar_convertion = round(dollar_convertion, 2)
#     dollar_convertion = str(dollar_convertion)
#     print("You have $" + dollar_convertion + " dollars")
# elif option == 2:
#     coin = input("How many uruguayan pesos do you have?")
#     coin = float(coin)
#     dolar_value = 41.80
#     dollar_convertion = coin / dolar_value
#     dollar_convertion = round(dollar_convertion, 2)
#     dollar_convertion = str(dollar_convertion)
#     print("You have $" + dollar_convertion + " dollars")
# elif option == 3:
#     coin = input("How many uruguayan pesos do you have?")
#     coin = float(coin)

#     dolar_value = 918.194
#     dollar_convertion = coin / dolar_value
#     dollar_convertion = round(dollar_convertion, 2)
#     dollar_convertion = str(dollar_convertion)
#     print("You have $" + dollar_convertion + " dollars")
# else:
#     option = str(option)
#     print("Invalid option: " + option)

def suma (a,b):
    print('Se suman dos numeros')
    resultado = a + b
    return resultado

sumatoria = suma (1, 4)
print (sumatoria)
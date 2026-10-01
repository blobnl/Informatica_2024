'''
operazioni elementari aritmetiche (// e %)
espressioni
operatori di assegnazione rapida
funzioni (math)
problemi di arrotondamento (e arrotondamento)
'''
num = 5
area = 7.45

risultato = 3 + (num + (5 -7/(area - 3 / 6)))**2

# calcolo risultato e resto di divisione intera
#numeroIn = input("inserire dividendo: ")
#dividendo = float(numeroIn)

dividendo = float(input("Inserire Dividendo: "))
divisore = float(input("Inserire divisore: "))

risultato = int(dividendo // divisore)
resto = dividendo % divisore

print("IL risultato della divisione tra", dividendo, "e", divisore, "è", risultato, 
      "con resto", resto)

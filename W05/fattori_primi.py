'''
dato un numero intero in input, creare una lista dei suoi fattori primi

ALGORTIMO: ??

'''

n = int(input("Inserisci un numero intero: "))
fattori = []
divisore = 2

while n > 1:
    if n % divisore == 0:
        fattori.append(divisore)
        n = n // divisore
    else:
        divisore += 1

print("I fattori primi sono:", fattori)
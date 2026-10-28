'''
1. Chiedete un numero intero N maggiore di 1
e stabilite se è primo

ALGORITMO
primo = true
per ogni numero tra 2 e floor(sqrt(N))
    se numero è divisore di N
        primo = falso
        
if primo --> stampa primo

2. Stampate tutti i numeri primi minori o uguali a un limite
M chiesto all'utente

'''
import math



M = int(input("Inserire numero: "))
for N in range(2, M + 1):
    # controlla se N è primo
    primo = True
    for divisore in range(2, math.floor(math.sqrt(N)) + 1):
        if N % divisore == 0:
            primo = False
            break
            
    if primo:
        print(f"{N} è un numero primo")
    #else:
    #    print(f"{N} NON è un numero primo")


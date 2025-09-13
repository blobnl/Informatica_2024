'''
stampare tabella potenze dei numeri....

dati NMAX e XMAX
stampa riga di intestazione
stampa matrice

per ogni valore dell'esponente
    stampa x^esponente (sulla stessa riga....)

per ogni valore numerico
    per ogni esponente
        stampa valore^esponente (sulla stessa riga...)

'''

NMAX = 5
XMAX = 12

# stampa intestazione
for esponente in range(1, NMAX + 1):
    stamp = f'X^{esponente}'
    print(f'{stamp:>8}', end = '')

print()

# stamp valori
for valore in range(1, XMAX + 1):
    for esponente in range(1, NMAX + 1):
        print(f'{valore**esponente:8d}', end = '')

    print()
'''
scrivere un programma che chiede all'utente una sequenza di valori interi 
maggiori di zero
(inserire un valore negativo per terminare la sequenza) e calcoli:
- media dei valori inseriti
- valore minimo
- valore massimo
'''
'''
valore = int(input("Inserire numero (-1 per terminare): "))
while valore >= 0:
    # istr
    valore = int(input("Inserire numero (-1 per terminare): "))
    '''

import math

finito = False
somma = 0
ctr = 0
massimo = -1
minimo = math.inf
while not finito:
    valore = int(input("Inserire numero (-1 per terminare): "))
    if valore < 0:
        finito = True
    else:
        # istr
        massimo = max(massimo, valore)
        minimo = min(minimo, valore)
        somma += valore #somma = somma + valore
        ctr += 1

if ctr > 0:
    print(f"la media dei numeri inseriti è {somma/ctr}")
    print(f"Il massimo della sequenza è {massimo}")
    print(f"Il minimo della sequenza è {minimo}")
else:
    print("Non sono stati inseriti numeri, non posso calcolare i valori richiesti")
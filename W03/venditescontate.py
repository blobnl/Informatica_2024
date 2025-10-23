'''
Un negozio di computer annuncia una nuova offerta chiamata 
«Kilobyte Day sale». L’offerta garantisce uno sconto dell’8% su tutti 
gli accessori per computer il cui prezzo è inferiore a $128, e del 16% 
se il prezzo è almeno $128.
Scrivere un programma che dato il prezzo di un accessorio, ne fornisce 
il prezzo scontato.
'''
'''
1. inserire costo oggetto
2. se costo < 128
    sconto = 8%
3. altrimenti
    sconto = 16%
costoScontato (1- sconto) * costo
stampa scontrino
'''

costo = float(input("Prezzo prodotto: "))
if costo < 128:
    sconto = 0.08
else:
    sconto = 0.16

prezzoScontato = (1 - sconto) * costo
print("Prezzo originale =", costo)
print("Prezzo scontato =", prezzoScontato)

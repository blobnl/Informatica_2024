''''
ricerca del primo elementoche corrisponde ad una determinata proprietà
'''

soglia = 10
insieme = [1, 4, 6, -4, -40, 12, 4, 6, 24, 18]
posizione = 0
trovato = False

'''
# gestione con for
for (indice, elemento) in enumerate(insieme):
    # verifico la proprietà...
    if elemento > soglia:
        posizione = indice
        trovato = True
        break
'''

# gestione con while
while posizione < len(insieme) and not trovato:
    if insieme[posizione] > soglia:
        trovato = True
    else:
        posizione += 1

if trovato:
    print(f"Valore maggiore di {soglia} in posizione {posizione}")
    print(insieme[posizione])
else:
    print("Nessun valore verifica la proprietà")


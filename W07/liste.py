'''
1. memorizzare in lista numeri inseriti da tastiera (q per terminare)
'''

valori = []
print('Inserire numeri (Q per terminare)')

finito = False
while not finito:
    dato = input('Dato: ')
    if dato.lower() == 'q':
        finito = True
    else:
        valori.append(int(dato))

print(f'Valori = ', end = '')
for idx in range(len(valori)):
    if idx == 0:
        print(valori[idx], sep = '', end = '')
    else:
        print(f', {valori[idx]}', sep = '', end = '')
print()

soglia = 10
trovato = False
idx = 0
while idx < len(valori) and not trovato:
    if valori[idx] > soglia:
        trovato = True
    else:
        idx += 1

if trovato:
    print(f'Trovato elemento maggiore di {soglia}: {valori[idx]} in posizione {idx}')
else:
    print(f'Nessun elemento maggiore di {soglia}')

# calcolo min e max senza usare le fx di python
massimo = valori[0]
idxMassimo = 0
minimo = valori[0]
idxMinimo = 0

for idx in range(1, len(valori)):
    valore = valori[idx]
    if valore > massimo:
        massimo = valore
        idxMassimo = idx
    if valore < minimo:
        minimo = valore
        idxMinimo = idx

print(f'Massimo = {massimo} in posizione {idxMassimo}')
print(f'Minimo = {minimo} in posizione {idxMinimo}')

pari = 0
dispari = 0
for dato in valori:
    if dato % 2 == 0:
        pari += 1
    else:
        dispari += 1

print(f'Numeri pari = {pari}, numeri dipsari = {dispari}')
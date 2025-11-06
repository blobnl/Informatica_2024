valori = []
finito = False
while not finito:
    dato = int(input("Inserire numero (-1 per terminare): "))
    if dato < 0:
        finito = True
    else:
        valori.append(dato)

if valori != []: # len(lavori) > 0 --> []: false --> valori
    media = sum(valori) / len(valori)
    massimo = max(valori)
    minimo = min(valori)
    print(f'{media=} {massimo=} {minimo=}')
else:
    print("nessun dato inserito")
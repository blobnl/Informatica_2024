totale = 0
contatore = 0

ok = True

while contatore < 10: # and ok:
    valore = int(input("Inserire dato: "))

    if valore < 0:
        continue

    if valore == 0:
       # ok = False
       break
    else:
        totale = totale + valore
    contatore = contatore + 1

print("Somma =", totale)
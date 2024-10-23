# rovare max tra n° inseriti da tastiera (termina con 0)

massimo = 0
ok = True
primoValore = True

while ok:
    valore = int(input("Valore = "))
    if valore == 0:
        ok = False
    else:
        # calcola il massimo
        if primoValore:
            massimo = valore
            primoValore = False
        else:
            if valore > massimo:
                massimo = valore
            # massimo = ma(massimo, valore)

print(f"IL valore massimo della sequenza è {massimo}")


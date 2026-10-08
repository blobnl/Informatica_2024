'''
ciclo a evento:
- stampa somma cifre numero intero inserito da tastiera
- media di valori (0 per terminare)
- registratore di cassa (fine per choudere scontrino)

'''

somma = 0
valori = 0

finito = False
while not finito:
    dato = float(input("valore: "))
    # 0 per terminare
    if dato == 0:
        finito = True
    else:
        somma = somma + dato
        valori = valori + 1
        
if valori == 0:
    print("Nessun valore inserito")
else:
    print("Media =", somma / valori)
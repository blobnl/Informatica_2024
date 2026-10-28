'''
liste come tabelle di corrispondenza
(tradurre insieme di indici --> valori corrispndenti)
evita:
if avolre == 0:
elif valore == 1:

esempio:
tradurre cifre numeriche in parole
0 -> "zero"
1 -> "uno"
etc...

'''
finito = False
while not finito:
    stringa = input("inserire cifra: ")
    if stringa == "":
        finito = True
        continue
    
    # else....
    cifra = int(stringa)
    cifre = ["zero", "uno", "due", "tre"]
    output = cifre[cifra]
    # etc....
    print(output)
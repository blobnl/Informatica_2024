'''
istruzioni per la gestione di condizioni particolari in un ciclo:
continue -> termina esecuzione iterazione corrente (torna a testare condizione)
break -> termina esecuzinoe del ciclo

NOTA: entrambe vanno chiamate SEMPRE E SOLO dopo aver testato una condizione
che puù determinare interruzione iterazinoe/ciclo

ESEMPIO:
inserire 10 numeri interi positivi e farne la media
- se il numero è negativo, saltarlo
- se il numero è 0, terminare il ciclo

'''

ITERAZIONI = 10
terminato = False

somma = 0
valori = 0
contatore = 0

while contatore < ITERAZIONI and not terminato:
    numero = input("Inserire numero: ")
    if numero == 0:
        terminato = True
    else:
        if numero > 0:
            somma += numero
            valori += 1
            contatore += 1


'''
# blocco con break e continue

while contatore < ITERAZIONI:
    numero = int(input("inserire numero: "))
    
    if numero < 0:
        continue
    
    if numero == 0:
        break
    
    somma += numero
    valori += 1
    contatore += 1
    
if contatore > 0:
    print("Media = ", somma / valori)
'''
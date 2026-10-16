'''
calolare il massimo (minimo) di una seuqenza di interi inseriti da tastiera
la sequenza termina quando si inserisce una stringa vuota

ALGORITMO??

fincheè non viene inserita riga vuota:
    se prima iterazione: massimo = valore inserito
    altrimenti massimo = max(massimo, valore inserito)
    
stampa massimo

'''

idx = 0
stringa = input("Inserisci valore: ")
while stringa != "":
    valore = int(stringa)
    if idx == 0:
        massimo = valore
        minimo = valore
    else:
        massimo = max(massimo, valore)
        minimo = min(minimo, valore)
    idx += 1
    stringa = input("Inserisci valore: ")
    
print(f"il massimo è {massimo}, il minimo è {minimo}")

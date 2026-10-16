'''
cicli misti con for --> break per terminare

fare la media di massimo 10 numeri inseriti da tastiera -> termine "" 
se numero negativo, saltalo
'''

somma = 0
valori = 0

for i in range(10):
    stringa = input("Inserisci valore: ")
    if stringa == "":
        break
    valore = int(stringa)
    
    if valore < 0:
        continue
    
    somma += valore
    valori += 1

print(f"Inseriti {valori} numeri")
if valori > 0:
    print(f"{somma/valori:.2f}")
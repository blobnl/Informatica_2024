'''
Algoritmi con lista:
cercare TUTTI gli elementi che verificano una condizione specifica

P1
Data una lista di contatti email_contatti = ["mario.rossi@gmail.com", "laura.bianchi@yahoo.it", 
    "stefano.verdi@gmail.com", "paolo.neri@outlook.com"] 
    crea una sola lista di utenti gmail da contattare via mail e 
    stampa l’elenco degli indirizzi, uno per riga, in rodine alfabetico

P2
Data la lista numeri = [14, 7, 3, 22, 19, 8, 31, 40], 
crea due liste di numeri pari e dispari, 
e calcola separatamente la somma delle due liste. 
Indica a schermo quale delle due liste ha somma maggiore


'''

email_contatti = ["laura.bianchi@yahoo.it", 
    "stefano.verdi@gmail.com", "mario.rossi@gmail.com", 
    "paolo.neri@outlook.com"]

email_google = []
for email in email_contatti:
    if email.lower().endswith("@gmail.com"):
        email_google.append(email)

'''       
email_google.sort()
for email in email_google:
    print(email)
'''
    
# opzione b
lista_ordinata = sorted(email_google)
for email in lista_ordinata:
    print(email)
print(email_google)


######################## problema 2
numeri = [14, 7, 3, 22, 19, 8, 31, 40]
pari = []
dispari = []

for numero in numeri:
    if numero % 2 == 0:
        pari.append(numero)
    else:
        dispari.append(numero)
        
print(pari, dispari)

print(f"Somma numeri pari = {sum(pari)}")
print(f"Somma numeri dispari = {sum(dispari)}")

if sum(pari) > sum(dispari):
    print("La lista dei pari ha somma maggiore")
elif sum(pari) == sum(dispari):
    print("Le somme sono uguali")
else:
    print("La lista dei dispari ha somma maggiore")
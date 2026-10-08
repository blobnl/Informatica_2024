'''
inserire numero e stampare tabellina

'''

'''
numero = int(input("inserisci numero: "))
moltiplicatore = 1

while moltiplicatore <= 10:
    print(numero, "*", moltiplicatore, "=", numero * moltiplicatore)
    moltiplicatore +=1
'''

'''
stampa rata e residuo di prestito
'''
prestito = int(input("prestito: "))
mesi = int(input("mesi: "))

contatore = 1
rata = prestito / mesi

while contatore <= mesi:
    prestito -= rata
    print("Rata:", rata, "RImanente:", prestito)
    contatore += 1

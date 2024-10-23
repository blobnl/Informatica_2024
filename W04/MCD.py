'''
inserire A e B
prova = min(A,B)
finchè prova non è divisore di A e B:
    prova = prova - 1

se prova != 1
    stampa prova come mcd
altrimenti
    stampa non esiste un mcd

'''

A = int(input("Inserire primo numero: "))
B = int(input("Inserire secondo numero: "))

prova = min(A, B)

while A % prova != 0 or B % prova != 0:
    prova = prova - 1

# uscita dal ciclo, 2 casi diversi
if prova != 1:
    print("Il MCD di", A, "e", B, "è", prova)
else:
    print("Non esiste un MCD tra", A, "e", B)

'''
. leggi a e b
2. mcd = minimo tra a e b
3. finchè mcd non è divisore di a e b e mcd > 1
    mcd = mcd - 1

4. se mcd == 1
    stampa no divisore comune
altrimenti
    stampa mcd
'''

A = int(input("inserire primo numero: "))
B = int(input("Inserire secondo numero: "))
MCD = min(A, B)

while not(A % MCD == 0 and B % MCD == 0) and (MCD > 1):
    MCD = MCD - 1

if MCD == 1:
    print(f"Non esiste un MCD tra {A} e {B}")
else:
    print(f"Il MCD tra {A} e {B} è {MCD}")
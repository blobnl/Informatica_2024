'''
Dato un numero ad N cifre (e.g., 1729), calcolare la somma delle sue cifre numeriche (-> 1+7+2+9)

Input: numero
Output: somma delle sue cifre

'''

numero = input("Inserire numero intero: ")
somma = 0
idx = 0

while idx < len(numero):
    valore = int(numero[idx])
    somma = somma + valore
    print(valore, somma)

    idx = idx + 1

print("somma cifre =", somma)
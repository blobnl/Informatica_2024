'''
insrire N
somma = 0
fichè n > 0
    cifra = n % 10
    somma = somma + cifra
    n = n // 10

stampa somma

'''
N = int(input("Inserire un numero: "))
somma = 0
numero = N

while N > 0:
    cifra = N % 10
    somma = somma + cifra
    N = N // 10
    print(f'{cifra} {somma} {N=}')

print(f"La somma delle cifre di {numero} è {somma}")

'''
N = input("Inserire numero: ")

somma = 0
for cifra in N:
    somma = somma + int(cifra)

print(f'La sooma delle cifre di {N} è {somma}')
'''
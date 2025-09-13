numero = int(input("Inserire numero: "))

somma = 0

while numero > 0:
    cifra = numero % 10
    numero = numero // 10
    somma = somma + cifra

    print(cifra, numero)

print("Somma =", somma)
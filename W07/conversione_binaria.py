'''
scrivere un programma che cobnverta un numero intero positivo
nella sua rappresentazione in binario puro
e la stampi su schermo

ALGORITMO:
?? n --> insieme di bit

'''

def convertiBinario(n):
    binario = ''
    while n > 0:
        resto = n % 2
        n = n // 2
        binario = str(resto) + binario
        
    return binario

def convertiIntero(binario):
    numero = 0
    for (idx, valore) in enumerate(binario):
        peso = len(binario) - 1 - idx
        numero += int(valore) * (2 ** peso)
        
    return numero

def main():
    finito = False
    while not finito:
        dato = input("Inserire valore: ")
        if dato == '':
            finito = True
            continue
        
        numero = int(dato)
        binario = convertiBinario(numero)
        conv = convertiIntero(binario)
        print(f"N = {numero} --> binario = {binario} --> {conv}")
    
    
main()
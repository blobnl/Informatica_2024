def filtra_multipli(lista, n):
    filtrati = []
    for valore in lista:
        if valore % n != 0:
            filtrati.append(valore)

    return filtrati

def main():
    numeri = [3, 6, 7, 9, 10, 12]
    print(filtra_multipli(numeri, 3))  
    # Output atteso: [7, 10]
    
main()

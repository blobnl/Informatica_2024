def somma_positivi(lista):
    trovati = 0
    somma = 0
    for valore in lista:
        if valore >= 0:
            somma += valore
            trovati += 1

    return (somma, trovati)


def main():
    numeri = [-3, 5, -2, 7, -9, 0]
    print(somma_positivi(numeri))  
    # Output atteso: (12, 3)

main()

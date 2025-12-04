def differenza_massima(lista):
    if lista == []:
        return 0
    
    return max(lista) - min(lista)

def main():
    numeri = [3, 7, 2, 9, 4]
    print(differenza_massima(numeri))  
    # Output atteso: 7  (perché 9 - 2 = 7)

main()

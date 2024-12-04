def intersezione_ordinata(l1, l2):
    intersezione = []
    for elemento in l1:
        if elemento in l2:
            intersezione.append(elemento)
    #intersezione.sort() return intersezione
    return sorted(intersezione)

# Funzione main per il test
def main():
    esempio1 = [10, 4, 7, 1]
    esempio2 = [4, 1, 6]
    print(intersezione_ordinata(esempio1, esempio2))  
    # Output atteso: [1, 4]

main()

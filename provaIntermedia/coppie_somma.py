def coppie_con_somma(lista, target):
    coppie = []
    # Da implementare
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            if lista[i] + lista[j] == target:
                coppie.append((lista[i], lista[j]))
    
    return coppie

def main():
    esempio = [1, 2, 3, 4, 5]
    target = 6
    print(coppie_con_somma(esempio, target))  
    # Output atteso: 2 coppie: (1, 5), (2, 4)
    
main()

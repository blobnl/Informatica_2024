def n_piu_grandi(lista, n):
    ordinata = sorted(lista, reverse = True)
    return ordinata[:n]

def main():
    esempio = [10, 4, 1, 3, 9, 7]
    n = 3
    print(n_piu_grandi(esempio, n))  
    # Output atteso: [10, 9, 7]

main()

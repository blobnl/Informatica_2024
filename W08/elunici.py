def elementi_unici(lista): 
    univoci = []
    for elemento in lista:
        if elemento not in univoci:
            univoci.append(elemento)

    return univoci

def main(): 
    numeri = [2, 4, 1, 2, 2, 3, 1, 4] 
    print(elementi_unici(numeri)) 
	# Output atteso: [1, 2, 3, 4] 

main()
def dividi_blocchi(lista, n):
   blocchi = []
   for i in range(0, len(lista), n):
      blocchi.append(lista[i:min(len(lista), i+n)])
   
   return blocchi

# Funzione main per il test
def main():
   esempio = [1, 2, 3, 4, 5, 6, 7]
   n = 3
   print(dividi_blocchi(esempio, n))  
   # Output atteso: [[1, 2, 3], [4, 5, 6], [7]]

main()

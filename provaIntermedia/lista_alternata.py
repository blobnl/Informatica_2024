def lista_alternata(l1, l2):
   lista = []
   for i in range(min(len(l1), len(l2))):
      lista = lista + [l1[i], l2[i]]

   for j in range(i+1, len(l1)):
      lista.append(l1[j])
   for j in range(i+1, len(l2)):
      lista.append(l2[j])
   
   return lista

# Funzione main per il test
def main():
   esempio1 = [1, 2, 3]
   esempio2 = ['a', 'b', 'c', 'd']
   print(lista_alternata(esempio1, esempio2))  
   # Output atteso: [1, 'a', 2, 'b', 3, 'c', 'd']

main()

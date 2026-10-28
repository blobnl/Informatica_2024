'''
Attenzione a come si gestiscono cancellazioni e cicli for
Il ciclo for su range per indice è inizializzato alla prima iterazione
--> se elimino un elemento è sicuro un errore 
(index out of range)

'''

lista = [2,3,4,5,6,7,8,9]
for i in range(len(lista)):
    if lista[i] % 2 == 0:
        lista.pop(i)
        
print(lista)

'''
Soluzioni:
1. gestire con while a contatore, e modificare indice solo se non rimuovo un elemento
2. creare lista temp con dati da tenere e poi ricopiare in lista originale
--> lista[:] = temp

'''
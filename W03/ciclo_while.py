# blocco inziale

#while condizione:
    # blocco di istruzioni esgeutio finchè la condizione è vera
    
# blocco successivo al ciclo

A = int(input("Inserire primo valore: "))
B = int(input("inserire secondo valore: "))

divisore = min(A, B) 
while not (A % divisore == 0 and B % divisore == 0) and divisore > 1:
     divisore -= 1
     
# dopo il ciclo testo valore divisore
if divisore == 1:
    print("non esiste MCD")
else:
    print("il MCD è", divisore)
    
    
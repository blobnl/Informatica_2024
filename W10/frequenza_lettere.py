'''
Data una frase letta da tastiera, e.g testo = "programmazione python", 
conta le occorrenze delle lettere contenute nella frase, 
e poi stampa l’elenco delle lettere presenti e della loro frequenza. 

NOTA: le lettere vanno contate indipendentemente dal fatto che 
siano minuscole o maiuscole 

'''




def frequenzaLettere(frase):
    occorrenze = {}
    frase = frase.lower()
    for car in frase:
        if car.isalpha():
            '''
            # inserimento o aggiornamento: opzione 1 con if else
            if car not in occorrenze:
                occorrenze[car] = 1
            else:
                occorrenze[car] = occorrenze[car] + 1   
            '''
            
            # inserimento o aggiornamento: opzione 2 con istruzione unica
            # se car non presente, la get restituisce 0 e inserisce valore 1
            # se car presente, incrementa il suo valore di 1
            occorrenze[car] = occorrenze.get(car, 0) + 1
                
    return occorrenze



def main():
    testo = input('Inserire frase: ')
    occorrenze = frequenzaLettere(testo)
    
    for (lettera, ripetizioni) in occorrenze.items():
        print(lettera, ripetizioni)

main()
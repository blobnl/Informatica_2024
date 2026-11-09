'''
MASTERMIND - Funzioni da completare in aula

Codice: quattro cifre diverse, scelte tra 1 e 6.
Segreto e tentativo sono stringhe, ad esempio "1234".
Massimo dieci tentativi validi.
Gli input non validi non consumano un tentativo.
'''



def leggi_tentativo():
    '''
    Chiede e restituisce un tentativo valido.
    Usare tentativo_valido e ripetere la richiesta se necessario.
    Ogni input deve avere un messaggio che spieghi cosa inserire.
    '''
    finito = False
    while not finito:
        codice = input("Inserire tentativo: ")
        if tentativo_valido(codice):
            finito = True
        else:
            print("Tentativo non valido")
        
            
    return codice

def tentativo_valido(codice):
    '''
    Restituisce True se il tentativo rispetta le regole.
    Controllare lunghezza, cifre ammesse e ripetizioni.
    '''
    if len(codice) != 4:
        return False
    if not codice.isdigit():
        return False
    
    for numero in codice:
        if numero not in "123456":
            return False
        
    return True



def valuta_tentativo(segreto, tentativo):
    '''
    Restituisce la tupla (corrette, fuori_posto).
    
    Esempio: segreto "1234", tentativo "1425": risultato (1, 2).
    '''
    corrette = 0
    presenti = 0
    
    for cifra in tentativo:
        if cifra in segreto:
            presenti += 1
            
    for i in range(len(segreto)):
        if segreto[i] == tentativo[i]:
            corrette += 1
            
    fuori_posto = presenti - corrette
    
    return (corrette, fuori_posto)
    
def numeroSegreto():
    return "1234"

def main():
    MAX_TENTATIVI = 10
    vinto = False
    
    segreto = numeroSegreto()
    for tentativo in range(MAX_TENTATIVI):
        codice = leggi_tentativo()
        #print(codice)
        (corrette, fuori_posto) = valuta_tentativo(segreto, codice)
        print(f"Tentativo {tentativo+1}: Corrette = {corrette} FP = {fuori_posto}")
        
        if corrette == 4:
            vinto = True
            break
        
    if vinto:
        print("Hai vinto")
    else:
        print("Hai perso")
        
        
main()
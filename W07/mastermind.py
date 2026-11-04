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
    pass

def tentativo_valido(tentativo):
    '''
    Restituisce True se il tentativo rispetta le regole.
    Controllare lunghezza, cifre ammesse e ripetizioni.
    '''
    pass



def valuta_tentativo(segreto, tentativo):
    '''
    Restituisce la tupla (corrette, fuori_posto).
    
    Esempio: segreto "1234", tentativo "1425": risultato (1, 2).
    '''
    pass


def gioca(segreto, massimo_tentativi=10):
    '''
    Mostrare le regole e gli indizi dopo ogni tentativo.
    Terminare con una vittoria quando le posizioni corrette sono quattro.
    Esauriti i tentativi, comunicare la sconfitta e mostrare il segreto.
    '''
    pass

def main():
    gioca("1234")

main()
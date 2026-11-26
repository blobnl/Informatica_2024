'''
stampa oridnata:

il file studenti.txt contiene per ogni riga matricola nome studente e voto esame separati da ';'
Scrivere un programma che stampi i dati:
- in ordine di matricola
- in ordine di nome
- in ordine (decrescente) di voto

'''

from operator import itemgetter

def creaDizionario(filename):
    studenti = {}
    with open(filename, 'r', encoding = 'utf-8') as file:
        for riga in file:
            parti = riga.strip().split(';')
            (mat, nome, voto) = (parti[0], parti[1], int(parti[2]))
            
            studenti[mat] = {"mat" : mat, "nome" : nome, "voto": voto}
            
    return studenti

def creaListaStudenti(filename):
    studenti = []
    with open(filename, 'r', encoding = 'utf-8') as file:
        for riga in file:
            parti = riga.strip().split(';')
            (mat, nome, voto) = (parti[0], parti[1], int(parti[2]))
            
            studente = {"mat" : mat, "nome" : nome, "voto": voto}
            studenti.append(studente)
            
    return studenti
        
        

def main():
    #elenco = creaDizionario('studenti.txt')
    elenco = creaListaStudenti('studenti.txt')
    
    elenco.sort(key = itemgetter("voto", "mat"))
    
    for studente in elenco:
        print(studente)
    
main()
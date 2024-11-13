'''
blackjack:
regole: giocatre vs computer, vengono distribuite le carte (coperte)
il giocatore continua a chiedere carte fino a quando o supera 21 (sballa) o si ferma
il banco continua a chidere carte fino a quando non arriva a un punteggio >= 17
il punteggio maggiore vince ( ameno che uno dei due giocatori non abbia superato 21). 
A parità di punti nn vince nessuno

ALGORITMO:
dai carte ai giocatori
gioca giocatore
se giocatore non ha sballato
    gioca banco
    verifica vinvita
altrimenti
    vinve banco

gioca giocatore:
    finchè punteggio < 21 e non mi sono fermato
        chiedi se gioactore vuole carta
        ae vuole carta
            estrai carta
            aggiorna punteggio
    restituire punteggio cgiocatore

gioca banco:
    finchè punteggio <= 17
        chiedi carta
        aggiorna punteggio


'''
import random

MAX_PUNTI = 21
MAX_PUNTI_BANCO = 17

# funzione che restituisce una carta estratta dal mazzo...
def estraiCarta(mazzo):
    carta = mazzo.pop()
    return carta

def giocaCiocatore(puntiGiocatore, mazzo):
    punti = puntiGiocatore
    print(f'Punti inizili giocatore = {punti}')

    finito = False
    while punti <= MAX_PUNTI and not finito:
        scelta = input('Altra carta (s/n)? ')
        if scelta.lower() == 'n':
            finito = True
        elif scelta.lower() == 's':
            carta = estraiCarta(mazzo)
            punti += carta
            print(f'Estratto {carta} punti: {punti}')
        else:
            print('Errore nell\'iserimento, devi mettere s o n')

    return punti
    

def giocaBanco(puntiBanco, mazzo):
    punti = puntiBanco
    print(f'Punti inizili banco = {punti}')

    while punti < MAX_PUNTI_BANCO:
        carta = estraiCarta(mazzo)
        punti += carta
        print(f'Estratto {carta} punti: {punti}')

    return punti

def creaMazzo():
    mazzo = list(range(1,11)) * 4
    random.shuffle(mazzo)

    return mazzo

def main():
    mazzo = creaMazzo()

    punteggioGiocatore = estraiCarta(mazzo)
    punteggioBanco = estraiCarta(mazzo)

    # gioca giocatore
    punteggioGiocatore = giocaCiocatore(punteggioGiocatore, mazzo)
    if punteggioGiocatore <= MAX_PUNTI:
        punteggioBanco = giocaBanco(punteggioBanco, mazzo)
        if punteggioBanco > MAX_PUNTI:
            print('VInce giocatore')
        elif punteggioBanco == punteggioGiocatore:
            print('parità')
        elif punteggioBanco < punteggioGiocatore:
            print('VInce giocatore')
        else:
            print('VInce banco')
    else:
            print('VInce banco')



main()
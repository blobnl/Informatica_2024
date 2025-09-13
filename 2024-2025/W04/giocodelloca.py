'''
gioco dell'oca con un solo giocatore:

casella = 0
finchè non ho superato la casella finale:
    lancia il dado
    aggiorna la posizione

stamoa fine partita

gioco dell'oca con due giocatori:

casella1 = 0
casella2 = 0
finchè un giocatore non ha superato la casella finale:
    lancia il dado per giocatore1
    aggiorna la posizione di g1
    se gicatore1 bon ha superato la fine
        lancia dado per g2
        aggiorna posizione g2

stamoa fine partita

'''
import random

casella1 = 0
casella2 = 0
FINE = 63

while casella1 <= FINE and casella2 <= FINE:
    dado = random.randint(1,6)
    casella1 = casella1 + dado 
    print(f"Giocatore 1: Dado = {dado} casella corrente = {casella1}")

    #if casella1 > FINE:
    #    continue
    if casella1 <= FINE:
        input("Premi enter per lanciare il dado ")
        dado = random.randint(1,6)
        casella2 += dado
        print(f"Giocatore 2: Dado = {dado} casella corrente = {casella2}")

    if casella2 <= FINE:
        input("Premi enter per lanciare il dado ")


if casella1 > casella2:
    print("Ha vinto il giocatore 1")
else:
    print("Ha vinto il giocatore 2")
    

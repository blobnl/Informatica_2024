'''
1. inserire lunghezza muro e piastrella
2. piastrelle = lunghMuro // lunghPiatrelle
3. se pastrelle è pari
    3.1 piastrelle = piastrelle - 1
4. calcola spazio rimanente
5. stampa output
'''

lunMuro = float(input("Lunghezza muro: "))
lunPiastrella = float(input("Lunghezza pastrella: "))

piastrelle = lunMuro // lunPiastrella

if piastrelle % 2 == 0:
    piastrelle = piastrelle - 1

spazioALato = (lunMuro - piastrelle * lunPiastrella) / 2



print("il numero totale di piastrelle è", piastrelle)
print("Lo spazio rimanente per ogni lato è", spazioALato)

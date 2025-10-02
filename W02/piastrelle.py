'''
calocalre numero piastrelle da posizionare in un numro, 
data la larghezza del muro e quella di ogni piastrella.
Il numero di piastrelle deve essere dispari. (BNBN....NB)
Calcolare anche lo spazio rimanente alle estremità 
(piastrelle devono essere centrate)
'''

larParete = 100
larPiastrella = 5
larCoppia = larPiastrella * 2

numCoppie = (larParete - larPiastrella) // larCoppia
piastrelle = numCoppie * 2 + 1
spazioRimanenete = (larParete - piastrelle * larPiastrella) / 2

print('Piastrelle = ', piastrelle)
print('Sapzio rimanente ai lati', spazioRimanenete)

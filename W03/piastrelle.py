'''
Bisogna posizionare lungo il muro una fila di piastrelle nere e bianche. 
Per ragioni estetiche l’architetto ha specificato che la prima e l’ultima piastrella 
devono essere nere. Il vostro compito è calcolare il numero di piastrelle necessarie 
e il vuoto a ciascuna delle due estremità della riga, dato lo spazio disponibile e 
la larghezza di ogni piastrella

soluzione ???
input -> larghezza muro e larghezza piastrella
output-> numero di paistrelle, spazio rimanente per lato

1. sapzio rimanente = larghMuro - larghPiastrella
2. coppie = spazio rimanente // (2 * larghPiastrella)
3. pastrelle = 2*coppie + 1
4. spaio a lato = (larghMuro - piatrelle * larghPiastrella) / 2
5. stampare i risultati

'''

larghezzaMuro = float(input("Lunghezza muro: "))
larghezzaPiastrella = float(input("Lunghezza piastrella: "))

spazioRImanente = larghezzaMuro - larghezzaPiastrella
coppie = spazioRImanente // (2 * larghezzaPiastrella)
piastrelle = int(2 * coppie + 1)

spazioALato = (larghezzaMuro - piastrelle * larghezzaPiastrella) / 2

print("il numero totale di piastrelle è", piastrelle)
print("Lo spazio rimanente per ogni lato è", spazioALato)
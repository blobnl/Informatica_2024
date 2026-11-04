'''
scrivere un programma che sia ingrado di comprimere e decomprimere 
una lista di valori interi con algoritmo RLE
sequenza --> insieme (valore, ripetizioni)

444433332221 --> (4,4)(4,3)(3,2)(1,0)

'''

def compressRLE(lista):
    pass
    
def expandRLE(compressed):
    pass
    
lista = [1,1,1,1,2,2,2,3,3,3,4,5,6]
compressed = compressRLE(lista)
expanded = expandRLE(compressed)
if lista == expanded:
    print("Lista espansa correttamente")
else:
    print("Errore in compressione/decompressione")
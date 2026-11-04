'''
Algoritmi con lista:
cercare il primo elemento che verifica uan condizione specifica
--> devo avere deu indicazioni: valore trovato, eventuale posizione del valore

es: data una lista = [...]
ricerca del primo numero > 100 (e se trovato restituire indice)

'''

lista = [1,2,3,4,115,6,7,8,9]

trovato = False
# indiceTrovato = -1
for (idx, valore) in enumerate(lista):
    # specifica condizione
    if valore > 100:
        trovato = True
        break
    
# usicta dal ciclo
if trovato:
    print(f"Traovato elemento {valore} in posizione {idx}")
    
## verifica che TUTTI i valori siano <= 100
valido = True
for (idx, valore) in enumerate(lista):
    # condizione NEGATA
    if valore > 100:
        valido = False
        break
    
if not valido:
    print(f"Insieme non valido per valore {valore} in posizione {idx}")
'''
Definisci una lista con elementi duplicati, 
ad esempio spesa = ["pane", "latte", "pane", "uova", "latte", "frutta"], 
e crea una nuova lista che non contenga duplicati. 
Stampa il numero di duplicati eliminati e poi la lista finale 
(senza duplicati)

'''
spesa = ["pane", "latte", "pane", "uova", "latte", "frutta"]
listaUnica = []

for item in spesa:
    if item not in listaUnica:
        listaUnica.append(item)
        
eliminati = len(spesa) - len(listaUnica)
print(f"Eliminati {eliminati} duplicati.\nLista item unici: {", ".join(listaUnica)}")
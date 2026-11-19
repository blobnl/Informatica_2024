'''
Insiemi:
- SD non ordinata e non indicizzata
- mutabile, ma può contenere solo dati immutabili
- non permettono duplicati

Creazione: {} set() {lista elementi}
Acesso agli elementi: 
- non possibile con indice, solo con for
- accesso a elenco ordinato --> passagio da lista con sorted()
Appartenenza: in
Aggiunta elementi:
- add() -> singolo elemento
- update() -> collezione (tupla, lista, set)
Ugugaglianza/differenza: verifica l'insieme di elementi non il loro ordine

Rimozione elemnto:
- remove() -> singolo elemento (eccezione se no presente)
- discard() -> singolo elemento (no eccezione)
- clear() -> elimina tutti gli elemnti dell'insieme

Funzioni su set:
- len() min/max() sum()
- sorted() -> genera lista ordinata

Operazioni tra insiemi:
- union()
- intersection()
- difference() -> operatore NON simmetrico
- issubset()/issuperset()

'''
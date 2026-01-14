ESSAY
Ritiro @m 0

TEXT
La piattaforma Exam <u>non prevede</u> la possibilità esplicita di ritirarsi dall'esame. Questa domanda serve proprio a questa funzione. Quindi, per segnalare la volontà di ritirarsi dall'esame, é sufficiente scrivere "**ritirato**" <u>nella risposta a questa domanda</u>. In caso di risposta vuota, il compito verrà corretto

TRUEFALSE
Scelta risultati prova intermedia @m 0

TEXT

Indicate nella risposta se volete utilizzare il **voto** acquisito nella **prova intermedia** come voto della parte di teoria dell'esame (**selezionate Vero**). Nel caso venga **selezionata la risposta Falso o non venga selezionata nessuna risposta**, il voto della parte di teoria sarà il risultato della correzione del compito. 

**NOTA 1:** non è possibile modificare la scelta sull'uso della valutazione intermedia DOPO la consegna del compito.

**NOTA 2:** nel caso venga selezionata come risposta Vero, siete pregati di **non rispondere alle domande di teoria**, in modo da semplificare la fase di correzione


ESSAY
Sistemi di numerazione

TEXT

Dati i numeri 23 e 37 (in base 10), convertirli in binario **su 6 bit** e sommarli. Indicare se l’operazione genera overflow e motivare la risposta.

ANSWER
Risposta: 

ESSAY
Architettura degli elaboratori

TEXT

Qual è il numero minimo di bit di Address Bus necessario per indirizzare una memoria da 4 GigaByte con un parallelismo di 32 bit?

ANSWER
Risposta: 

ESSAY
Python

TEXT
Il linguaggio Python mette a disposizione dei programmatori **dizionari** (`dict`) e **insiemi** (`set`). Si richiede di fornire una sintetica descrizione di queste due strutture dati complesse, indicando almeno una caratteristiche comune.

ANSWER
Risposta: 


CHEATSHEET
ita

QUESTION
Grafico a Barre Testuale

TEXT
Scrivere un programma in Python in grado di generare un **grafico a barre orizzontali in modalità testuale**. Il programma deve generare il grafico leggendo i dati da due file:

- **Un file CSV** contenente le etichette e i valori da visualizzare.
- **Un file di configurazione** che definisce le impostazioni (in un formato `key=value`)  per la generazione del grafico.

Il grafico dovrà essere stampato nel terminale, **utilizzando solo testo**, senza alcuna libreria grafica. Il grafico deve essere diviso in due parti che contengono: 

1) **le etichette dei dati**, che devono essere allineati (si assume che la lunghezza massima dell'etichetta sia 20 caratteri), e 
2) **le barre corrispondenti ai valori associati alle etichette**, normalizzati rispetto al numero massimo di caratteri (quindi, se sono richiesti 30 caratteri per il grafico, la barra corrispondente al valore massimo avrà una lunghezza di 30 caratteri, e le altre avranno una lunghezza proporzionale).

I nomi dei due file (file di dati e file di configurazione) sono definiti nel codice come costanti.



## Specifiche

Il file con i dati è un file CSV che contiene per ogni riga una etichetta e il valore corrispondente separati da virgola. Il file CSV contiene un'intestazione, e un esempio di file è il seguente (`dati.csv`):

```
label,value
Apples,30
Bananas,15
Cherries,25
Dates,10
```

Il file di configurazione può contenere le seguenti chiavi:

- `max_bar_length`: la lunghezza (in caratteri) della barra più lunga (**default: 50**)
- `bar_char`: il carattere da utilizzare per disegnare la barra (**default: `*`**)
- `show_values`: se `true`, stampa il valore numerico alla fine di ogni barra, se `false` no (**default: `true`**)
- `sort`: se `asc` o `desc`, ordina i dati in ordine crescente o decrescente (**default: nessun ordinamento**)
- `title`: se presente, visualizza un titolo sopra il grafico (**default: riga vuota**)

Se una chiave **non è specificata** nel file di configurazione, allora si assume che al parametro venga assegnato il suo **valore di default**. 

Si assume che sia il file di dati che il file di configurazione **NON contengano errori** al loro interno (e quindi, NON è necessario fare controlli sul loro formato).


### Esempi di file di configurazione

**Esempio 1 – `config1.txt`:**
```
bar_char=#
show_values=true
sort=desc
title=Frutta Ordinata per Quantità
```



**Esempio 2 – `config2.txt`:**
```
max_bar_length=60
bar_char=-
show_values=false
sort=asc
```



## Uscita Attesa

Con il file CSV `dati.csv` e la configurazione `config1.txt`, l'output nel terminale sarà il seguente:

```
Frutta Ordinata per Quantità
Apples               | ################################################## 30
Cherries             | ######################################### 25
Bananas              | ######################### 15
Dates                | ################ 10
```

Con lo stesso file di dati e `config2.txt` come file di configurazione, l'output sarà invece:

```
Dates              | ---------------
Bananas            | -------------------------
Cherries           | -------------------------------------
Apples             | ------------------------------------------------------------
```

FILES
dati.csv
config1.txt
config2.txt
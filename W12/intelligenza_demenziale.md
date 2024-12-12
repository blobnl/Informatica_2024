# Intelligenza Demenziale

Dopo il successo di ChatGPT, un ricercatore vuole sviluppare un nuovo algoritmo di intelligenza artificiale, che sia in grado di scrivere delle opere letterarie come la Divina Commedia o i Promessi Sposi.

A tal fine, il ricercatore dispone di un file di testo contenente il testo integrale delle opere letterarie. Il programma deve leggere il testo di una di tali opere, ed apprendere le "frequenze dei 2-lemmi" presenti nel testo, ossia la frequenza con cui compaiono tutte le possibili coppie di parole **consecutive**.
Nell'elaborare i testi, si consideri il testo come completamente minuscolo, e si trattino tutti i simboli di punteggiatura come se fossero degli spazi (*1).

*Ad esempio, ne "I Promessi Sposi", la coppia di lemmi "`si può`" compare 65 volte, la coppia "`la parentela`" compare 3 volte, la coppia "`riflessione dubitativa`" 1 sola volta, e così via.*

Una volta calcolate le frequenze delle coppie consecutive di lemmi, il programma deve generare un testo "verosimile" con le seguenti regole:

1. l'utente deve inserire una qualsiasi parola. Se questa parola non compare nel testo, essa viene sostituita dal programma con una parola casuale tra quelle presenti nel testo
2. partendo dalla parola del punto 1, il programma identifica la parola successiva, considerando tutte le coppie di lemmi che iniziano con la prima parola, e scegliendo una parola a caso tra le 5 più frequenti (*2).
3. ripetere il passo 2, partendo da quest'ultima parola trovata, fino ad ottenere una frase di lunghezza casuale tra 5 e 50 parole.
4. ripetere dal punto 1, finché l'utente non inserisce una riga vuota.

NOTE:
- (*1) i simboli di punteggiatura sono definiti dalla costante `string.punctuation`
- (*2) nel testo dei Promessi Sposi, alla parola "don" segue "abbondio" per 233 volte, "rodrigo" 137 volte, "ferrante" 24 volte, "gonzalo" 20 volte, "filippo" 3 volte, "pietro" 2 volte, e così via. Il programma sceglierà casualmente uno dei primi 5 nomi, tra quelli con maggior frequenza. Nel caso in cui ci siano meno di 5 successori, si scelga casualmente tra quelli presenti. Nel caso in cui vi siano molti successori con la stessa frequenza, si scelga arbitrariamente.

### Esempio

Se il programma viene addestrato con il testo `promessisposi.txt`, esso potrà presentare le seguenti interazioni (essendoci un fattore casuale, i testi saranno ogni volta diversi):

```
Parola: lago
giaceva consolatevi gli disse renzo si può dir di quel momento e con le parole non è una voce che 
Parola: don
rodrigo il cardinale e non si trovava nel suo paese la mano in un po meglio che non si fosse stata in fretta la mano al padre molto più a cui la sua strada di nuovo in una mano al padre guardiano
Parola: don
abbondio e non era un uomo da quel che si fermò ad essa non ci si fosse una certa distanza a cui la mano in un gran parte di più di non so quel che si 
Parola: ramo
dalbero né con la mano in quella parte a far qualche tempo che la cosa è qui non si può far le donne e di più in fretta a un 
Parola: ramo
dalbero né anche di quel tempo che si fermò su quel momento si può esser veduto che si mise la quale si può far di non so anchio che non ci sia 
Parola:
```


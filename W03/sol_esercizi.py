'''
Chiedi all’utente di inserire due variabili utente e 
password. Se il nome utente è "admin" e la password 
è "segreta123", stampa "Accesso consentito". In caso 
contrario, stampa "Credenziali errate".
'''

UTENTE = "admin"
PWD = "segreta123"

user = input("User: ")
password = input("Password: ")

if user == UTENTE and password == PWD:
    print("Accesso consentito")
else:
    print("accesso negato")

'''

Chiedi all’utente di inserire una stringa ruolo. Crea un programma che valuti  il valore della stringa:
Se ruolo è uguale a "admin", stampa "Accesso completo al sistema".
Se ruolo è uguale a "editor", stampa "Accesso limitato alla gestione dei contenuti".
Se ruolo è uguale a "ospite", stampa "Accesso in sola lettura".
In tutti gli altri casi, stampa "Ruolo non riconosciuto".
'''

# si risolve con if...elif...elif...else

'''
Chiedi all’utente di inserire una mail. 
Se la stringa inserita è vuota, 
stampa un messaggio di errore, 
se l’indirizzo mail termina con «@gmail.com» 
stampa la scritta «Account riconosciuto», 
altrimenti stampa «Account invalido»

'''

mail = input("Mail: ")

if mail == '':
    print("Errore: mail vuota")
elif mail.endswith('@gmail.com'): # ig '@gmail.com' in mail:
    print("Account riconosciuto")
else:
    print("Account non valido")

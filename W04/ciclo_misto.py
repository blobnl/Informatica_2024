'''
ciclo basato su numero di iterazioni E evento
Ad esempio:
inserimento pin dello smartphone con max 3 tentativi
(e verifica di QUALE condizione ha determinato uscita 
dal ciclo)

'''
PIN = '1234'
MAX_TENTATIVI = 3

pin_corretto = False
prove = 0

while not pin_corretto and prove < 3:
    inserito = input("Inserire pin: ")
    if inserito == PIN:
        pin_corretto = True
    else:
        print("PIN errato")
        prove += 1 # prove = prove + 1
        
if prove == 3:
    print("Numero massimo di tentativi esaurito...")
else:
    print("PIN corretto, accesso garantito")

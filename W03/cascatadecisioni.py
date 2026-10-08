'''

Scala richter: in base al valore inserito dall'utente, stampare effetti:
| Valore| Effetto |
| 8     | La maggior parte delle strutture cade |
| 7     | Molti edifici vengono distrutti |
| 6     | Molti edifici vengono significativamente danneggiati e alcuni collassano |
| 4,5   | Danni a edifici costruiti in modo non adeguato |

'''

'''
alcolico = input("ALcolico? (si/no) = ")

if alcolico == 'si':
    eta = int(input("Età = "))
    if eta >= 21:
        print("Servi alcolico")
    else:
        print("Non si fa...")
else:
    print("Srevi non alcolico")

'''

# richetr

richter = float(input("Inserire intesnità terremoto: "))

if richter > 8.0:
    print('La maggior parte delle strutture cade')
elif richter >= 7.0:
    print("molto grave")
elif richter > 6.0:
    print("Abbastanza grave")
elif richter > 4:
    print("qualche danno")
else:
    # quando nessun delle condiz precedenti è verificata
    print("nessun danno")
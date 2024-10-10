'''
>= 8
tra 7 e 8
tra 6 e 7
tra 4.5 e 6
sotto 4.5
'''

richter = float(input("Magnitudine teeremoto: "))

if richter >= 8.0:
    print("casca tutto")
elif richter >= 7.0:
    print("molti edifici distrutti")
elif richter >= 6.0:
    print("Molti edific danneggiati")
elif richter >= 4.5:
    print("qualche danno")
else:
    print("Nessun danno")
    

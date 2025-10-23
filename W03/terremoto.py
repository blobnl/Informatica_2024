val = float(input("Valore Richter: "))

if val >= 8.0:
    print("tutto distrutto")
elif val >= 7.0:
    print("molti danni")
elif val >= 6.0:
    print("qualche danno")
else:
    print("nessun danno")
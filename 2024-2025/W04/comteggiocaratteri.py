riga = input("Inserire una stringa: ")

alfabetici = 0
vocali = 0
consonanti = 0

for carattere in riga:
    if carattere.isalpha():
        alfabetici = alfabetici + 1

        if carattere.lower() in "aieou":
            vocali = vocali + 1
        else:
            consonanti = consonanti + 1

print(f"Acaratteri alfabetici = {alfabetici}")
print(f"Vocali = {vocali}")
print(f"Consonanti = {consonanti}")


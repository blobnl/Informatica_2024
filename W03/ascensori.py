floor = int(input("Inserire piano: "))

actualFloor = floor

if floor > 13:
    actualFloor = floor - 1

print("Il piano", floor, "corrisponde al piano", actualFloor)
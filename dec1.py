lines = []

while 1:
    line = input("Input number, enter empty to finish \r\n")
    if line == '':
        break
    lines.append(line)

dailPosition = 50
totalZeroPosition = 0
for line in lines:
    isRightRotation = line[0] == 'R'
    number = int(line[1:])

    floor = abs(number // 100)
    if (isRightRotation):
        if dailPosition != 0 and dailPosition + number > 100:
            print (f'Went from {dailPosition} to {dailPosition + number} counting up')
            totalZeroPosition += 1
            floor -= 1

        dailPosition = (dailPosition + number) % 100
    else:
        if dailPosition != 0 and dailPosition - number < 0:
            print (f'Went from {dailPosition} to {dailPosition - number} counting up')
            totalZeroPosition += 1
            floor -= 1

        dailPosition = (dailPosition - number) % 100
    
    if dailPosition == 0:
        print (f"Position is zero from instruction {line}")
        totalZeroPosition += 1

    if floor > 0:
        print(f"Multipass {floor} times")
        totalZeroPosition += (floor)
    

print (f'Total zero Position: {totalZeroPosition}')
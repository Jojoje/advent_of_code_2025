lines = []

while 1:
    line = input("Input number, enter empty to finish \r\n")
    if line == '':
        break
    lines.append(line)

dailPosition = 50
totalZeroPosition = 0
for line in lines:
    lastPosition = dailPosition
    isRightRotation = line[0] == 'R'
    number = int(line[1:])

    floor = abs(number // 100)
    if (isRightRotation):
        if dailPosition != 0 and dailPosition + number > 100:
            totalZeroPosition += 1
            floor -= 1

        dailPosition = (dailPosition + number) % 100
    else:
        if dailPosition != 0 and dailPosition - number < 0:
            totalZeroPosition += 1
            floor -= 1

        dailPosition = (dailPosition - number) % 100
    
    if dailPosition == 0:
        totalZeroPosition += 1

    if floor > 0:
        if number % 100 == 0 and dailPosition == 0:
            floor -= 1
        totalZeroPosition += (floor)

    print(f'Current: {lastPosition}, instruction: {line}, new position: {dailPosition}, current zero count {totalZeroPosition}')

    
print (f'Total zero Position: {totalZeroPosition}')
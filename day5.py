data = [line.strip() for line in open("input.txt", 'r')]

counter = 0
pos = [0, 0]
arrow = '->'
rightPos = []
leftPos = []
theMap = {}


for i, line in enumerate(data):
    words = line.split(" ")
    leftPos.append([int(words[0].split(',')[0]), int(words[0].split(',')[1])])
    rightPos.append([int(words[2].split(',')[0]), int(words[2].split(',')[1])])

for i in range(len(rightPos)):
    while leftPos[i][0] != rightPos[i][0] or leftPos[i][1] != rightPos[i][1]:
        string = ''.join(str(leftPos[i]))
        if string in theMap:
            theMap[string] += 1
        else:
            theMap[string] = 1
        if leftPos[i][1] < rightPos[i][1]:
            leftPos[i][1] += 1
        elif leftPos[i][1] > rightPos[i][1]:
            leftPos[i][1] -= 1
        if leftPos[i][0] < rightPos[i][0]:
            leftPos[i][0] += 1
        elif leftPos[i][0] > rightPos[i][0]:
            leftPos[i][0] -= 1
    string = ''.join(str(leftPos[i]))
    if string in theMap:
        theMap[string] += 1
    else:
        theMap[string] = 1
            


for i in theMap.values():
    if i > 1:
        counter += 1

print(counter)


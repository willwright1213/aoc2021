# let the input describe a a list of numeral input, 1 per line, where it forms a series of vectors of size 3
# for every new line, begins a new vector, and the same vector's next 2 elements are the next two lines 
# because there's necessarily an overlap of 2 values between the nth vector and n-1 vector,
# we only need to compare v_n[size -1] with v_(n-1)[0]


# To achieve this I made a circular array which at first will store the first 3 elements of the list (the first vector).
# starting from the 4th element (index 3), each value will be compared to postion 0..2 circularly. This is what simulates
# our v_n[size -1] > v_(n-1)[0] comparison to see if the sum of v_n is bigger than the sum of v_(n-1)

data = [line.strip() for line in open("input.txt", 'r')]

count = 0
bingoCalls = None
bingoBoard = []
bingoBoards = []

def winnerRow(board, lpr, lpc):
    for i in range(len(board[lpr])):
        if board[lpr][i][len(board[lpr][i]) -1] != '.':
            return False
    return True

def winnerCol(board, lpr, lpc):
    for i in range(len(board)):
        if board[i][lpc][len(board[i][lpc]) -1] != '.':
            return False
    return True


for i, line in enumerate(data):
    if i == 0:
        bingoCalls = line.split(',')
        continue;
    elif line == '' and i > 1:
        bingoBoards.append(bingoBoard)
        bingoBoard = []
        continue;
    elif i >= 2:
        numbers = " ".join(line.split()).split()
        bingoBoard.append(numbers)

bingoBoards.append(bingoBoard)


def findWinningBoard():
    for number in bingoCalls:
        for i in range(len(bingoBoards)):
            if bingoBoards[i] == None:
                continue
            for j in range(len(bingoBoards[i])):
                for y in range(len(bingoBoards[i][j])):
                    if bingoBoards[i][j][y] == number:
                        bingoBoards[i][j][y] = bingoBoards[i][j][y] + "."
                        if winnerRow(bingoBoards[i], j, y):
                            return number, bingoBoards[i], i
                        if winnerCol(bingoBoards[i], j, y):
                            return number, bingoBoards[i], i
    return None, None, None

winningBoards = 0

while len(bingoBoards) > winningBoards: 
    number, winnerBoard, i = findWinningBoard()
    bingoBoards[i] = None
    winningBoards += 1


sum = 0

for row in winnerBoard:
    for val in row:
        if '.' not in val:
            sum += int(val)

print(sum * int(number))

print(numbers)

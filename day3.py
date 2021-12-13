# let the input describe a a list of numeral input, 1 per line, where it forms a series of vectors of size 3
# for every new line, begins a new vector, and the same vector's next 2 elements are the next two lines 
# because there's necessarily an overlap of 2 values between the nth vector and n-1 vector,
# we only need to compare v_n[size -1] with v_(n-1)[0]


# To achieve this I made a circular array which at first will store the first 3 elements of the list (the first vector).
# starting from the 4th element (index 3), each value will be compared to postion 0..2 circularly. This is what simulates
# our v_n[size -1] > v_(n-1)[0] comparison to see if the sum of v_n is bigger than the sum of v_(n-1)

data = [line.strip() for line in open("input.txt", 'r')]

triplets = [0,0,0]
count = 0
gamma = 0
epsilon = 0
numbers = []

for i, line in enumerate(data):
    numbers.append(line)

eliminated = 0

for i in range(12):
    oneCount = 0;
    zeroCount = 0;
    if eliminated == 999:
        break
    for j in range(len(numbers)):
        if numbers[j] != 'na':
            if int(numbers[j][i]) & 1 == 1:
                oneCount += 1
            else:
                zeroCount += 1
    print(str(zeroCount) + " : " + str(oneCount))
    
    if oneCount < zeroCount:
        for y in range(len(numbers)):
            if eliminated == 999:
                break
            if numbers[y] != 'na':
                if int(numbers[y][i]) & 1 == 0:
                    numbers[y] = 'na'
                    eliminated += 1
    elif zeroCount < oneCount:
        for z in range(len(numbers) - 1):
            if eliminated == 999:
                break
            if numbers[z] != 'na':
                if int(numbers[z][i]) & 1 == 1:
                    numbers[z] = 'na'
                    eliminated += 1
    else:
        print("yo")
        for y in range(len(numbers)):
            if eliminated == 999:
                break
            if numbers[y] != 'na':
                if int(numbers[y][i]) & 1 == 1:
                    numbers[y] = 'na'
                    eliminated += 1


print(numbers)
#0b100111110011
#0b001011100001



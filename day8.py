data = [line.strip() for line in open("input.txt", 'r')]

counter = 0
pos = [0, 0]
segments = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
digit  =  [0,0,0,0,0,0,0]
letters = ['a','b','c','d','e','f','g']

for i, line in enumerate(data):
    map = [0,0,0,0,0,0,0,0,0,0]
    words = line.split("|")
    output = words[1].strip().split(" ")
    input = words[0].strip().split(" ")
    sinput = sorted(input, key=len)
    one = sinput[0]
    seven = sinput[1]
    four = sinput[2]
    eight = sinput[9]
    fullDigits = ""
    for o in output:
        if len(o) == 7:
            fullDigits += "8"
        if len(o) == 6:
            if one[0] not in o or one[1] not in o:
                fullDigits += "6"
                print(o + " " + one)
            elif four[0] not in o or four[1] not in o or four[2]  not in o or four[3] not in o:
                fullDigits += "0"
            else:
                fullDigits += "9"
        if len(o) == 5:
            if one[0] in o and one[1] in o:
                fullDigits += "3"
            else:
                i = 0
                for c in four:
                    if c not in o:
                        i += 1
                if i == 2:
                    fullDigits += "2"
                else:
                    fullDigits += "5"
        if len(o) == 4:
            fullDigits += "4"
        if len(o) == 3:
            fullDigits += "7"
        if len(o) == 2:
            fullDigits += "1"
    counter += int(fullDigits)
    print(fullDigits)
                
                

            

print(counter)

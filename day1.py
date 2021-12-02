data = [line.strip() for line in open("input.txt", 'r')]

triplets = [0,0,0]
count = 0

for i, line in enumerate(data):
    number = int(line)
    if i > 2:
        if number > triplets[i % 3]:
            increasedCount += 1
    triplets[i % 3] = number
    i += 1
        

print(increasedCount)

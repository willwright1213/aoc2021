import numpy

counter = [0]
dumbo = []

flashed = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
      ]

def increaseStep(dumbo, flashed,i,j, step):
    if i < 0 or i > 9 or j < 0 or j > 9:
        return
    if flashed[i][j] == step:
        return
    if dumbo[i][j] == 9:
        dumbo[i][j] = 0
        counter[0] += 1
        flashed[i][j] = step
        increaseStep(dumbo, flashed, i+1, j-1, step)
        increaseStep(dumbo, flashed, i+1, j+1, step)
        increaseStep(dumbo, flashed, i+1, j, step)
        increaseStep(dumbo, flashed, i-1, j-1, step)
        increaseStep(dumbo, flashed, i-1, j+1, step)
        increaseStep(dumbo, flashed, i-1, j, step)
        increaseStep(dumbo, flashed, i, j-1, step)
        increaseStep(dumbo, flashed, i, j+1, step)
        return
    dumbo[i][j] += 1
    

data = [line.strip() for line in open("input.txt", 'r')]


for i, line in enumerate(data):
    row = []
    for n in line:
        row.append(int(n))
    dumbo.append(row)
    
found = False
for i in range(1, 1000):
    if found == True:
        break
    for j in range(10):
        if found == True:
            break
        for k in range(10):
            f = counter[0]
            increaseStep(dumbo, flashed,j,k, i)
            if counter[0] - f == 100:
                print(i)
                found = True
                break

print(counter)

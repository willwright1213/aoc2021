import numpy

data = [line.strip() for line in open("input.txt", 'r')]

count = 0
lowPoints = []
map = []

for i, line in enumerate(data):
    row = []
    for val in line:
        row.append(int(val))
    map.append(row)


for i in range(len(map)):
    for j in range(len(map[1])):
        if i == 0:
            if j == 0:
                if map[i][j] < map[i][j+1] and  map[i][j] < map[i+1][j]:
                    lowPoints.append([i,j])
            elif j == len(row) - 1:
                if map[i][j] < map[i][j-1] and  map[i][j] < map[i+1][j]:
                    lowPoints.append([i,j])
            else:
                if map[i][j] < map[i][j-1] and map[i][j] < map[i][j+1] and map[i][j] < map[i+1][j]:
                    lowPoints.append([i,j])
        elif i == len(map) - 1:
            if j == 0:
                if map[i][j] < map[i][j+1] and  map[i][j] < map[i-1][j]:
                    lowPoints.append([i,j])
            elif j == len(row) - 1:
                if map[i][j] < map[i][j-1] and  map[i][j] < map[i-1][j]:
                    lowPoints.append([i,j])
            else:
                if map[i][j] < map[i][j-1] and map[i][j] < map[i][j+1] and map[i][j] < map[i-1][j]:
                    lowPoints.append([i,j])
        else:
            if j == 0:
                if map[i][j] < map[i][j+1] and  map[i][j] < map[i-1][j] and map[i][j] < map[i+1][j]:
                    lowPoints.append([i,j])
            elif j == len(row) - 1:
                if map[i][j] < map[i][j-1] and  map[i][j] < map[i-1][j] and map[i][j] < map[i+1][j]:
                    lowPoints.append([i,j])
            else:
                if map[i][j] < map[i][j-1] and map[i][j] < map[i][j+1] and map[i][j] < map[i-1][j] and map[i][j] < map[i+1][j]:
                    lowPoints.append([i,j])
    



def recursiveBasinSize(map, i, j, size, visited=[]):
    visited.append([i,j])
    if j < len(map[i]) - 1:
        if map[i][j] < map[i][j+1] % 9 and [i,j+1] not in visited:
            visited = recursiveBasinSize(map,i,j+1, size, visited)
    if j > 0:
        if map[i][j] < map[i][j-1] % 9  and [i,j-1] not in visited:
            visited = recursiveBasinSize(map,i,j-1, size, visited)
    if i < len(map) - 1:
        if map[i][j] < map[i+1][j] % 9  and [i+1,j] not in visited:
            size += 1
            visited = recursiveBasinSize(map,i+1,j, size, visited)
    if i > 0:
        if map[i][j] < map[i-1][j] % 9  and [i-1,j] not in visited:
            size += 1
            visited = recursiveBasinSize(map,i-1,j, size, visited)
    return visited


biggest = [0,0,0]

for coord in lowPoints:
    visited = []
    visited = recursiveBasinSize(map, coord[0], coord[1], 0, visited);
    if(len(visited) > biggest[2]):
        biggest.append(len(visited))
        biggest.pop(0)
    elif(len(visited) > biggest[1]):
        biggest.append(len(visited))
        biggest.pop(0)
    elif(len(visited) > biggest[0]):
        biggest[0] = len(visited)

print(numpy.prod(biggest))

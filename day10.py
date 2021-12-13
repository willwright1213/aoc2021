import numpy

data = [line.strip() for line in open("input.txt", 'r')]


for i, line in enumerate(data):
    words = line.split(' ')

print(numpy.sort(counts)[len(counts)//2])

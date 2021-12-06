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

for i, line in enumerate(data):
    number = int(line)
    if i > 2:
        if number > triplets[i % 3]:
            count += 1
    triplets[i % 3] = number
 

print(count)

depths = open('input').readlines()

number_of_increments = 0
previous = -1000

for depth in depths:
    depth = int(depth)
    if previous != -1000 and depth > previous:
        number_of_increments += 1
    previous = depth

print(number_of_increments)

depths = open('input').readlines()

number_of_increments = 0
previous = -1000

for depth in depths:
    depth = int(depth)
    if previous != -1000 and depth > previous:
        number_of_increments += 1
    previous = depth

print(number_of_increments)

# I'm just learning Python, and I found out there is a one liner solution
depth_increased = len([depth for index, depth in enumerate(depths) if int(depth) > int(depths[index - 1])])
print(depth_increased)

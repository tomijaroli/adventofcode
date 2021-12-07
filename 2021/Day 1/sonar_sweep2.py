depths = open('input').readlines()

number_of_increments = 0
previous_sum = -1000

for index, depth in enumerate(depths):
    window = [int(depth) for depth in depths[index:index+3]]
    sum_of_windows = sum(window)

    if previous_sum != -1000 and sum_of_windows > previous_sum:
        number_of_increments += 1

    previous_sum = sum_of_windows

print(number_of_increments)

# I'm just learning Python, and I found out there is a one liner solution
depths_increased = sum((int(a) < int(d) for a, d in zip(depths, depths[3:])))
print(depths_increased)

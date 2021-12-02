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

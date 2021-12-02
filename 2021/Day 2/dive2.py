x = depth = aim = 0

for move in open('input').readlines():
    direction, unit = move.strip().split(' ')
    unit = int(unit)

    if "forward" in direction:
        x += unit
        depth += (unit * aim)
    elif "up" in direction:
        aim -= unit
    elif "down" in direction:
        aim += unit

print(x * depth)

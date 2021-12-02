x = y = 0

for move in open('input').readlines():
    direction, unit = move.split(' ')
    unit = int(unit)

    if "forward" in direction:
        x += unit
    elif "up" in direction:
        y -= unit
    elif "down" in direction:
        y += unit

print(x * y)

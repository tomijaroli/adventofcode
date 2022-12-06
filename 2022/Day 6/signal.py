input = open('input', 'r').read()

def solve(window_size):
    for index in range(len(input)):
        window = [ character for character in input[index:index + window_size] ]
        if len(set(window)) == len(window):
            return index + window_size

print(solve(4))
print(solve(14))


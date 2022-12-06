import re
with open('input', 'r') as input:
    instructions = input.readlines()

instructions = [ list(map(int, re.findall('\d+', line))) for line in instructions[10:] ]

stacks = [
    'RGJBTVZ',
    'JRVL',
    'SQF',
    'ZHNLFVQG',
    'RQTJCSMW',
    'SWTCHF',
    'DZCVFNJ',
    'LGZDWRFQ',
    'JBWVP'
]

def solve(stacks, is9000):
    stacks = list(stacks)
    for amount, starting, target in instructions:
        top = stacks[starting - 1][-amount:]
        if is9000:
            top = top[::-1]
        stacks[starting - 1] = stacks[starting - 1][:-amount]
        stacks[target - 1] += top
    return ''.join(stack[-1] for stack in stacks)

print(solve(stacks, True))
print(solve(stacks, False))

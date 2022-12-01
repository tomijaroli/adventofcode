input = open('input').read().split('\n\n')
elvesInventories = [ list(map(int, line.splitlines())) for line in input ]

sortedSumCalories = sorted([ sum(elf) for elf in elvesInventories ], reverse=True)

print(sortedSumCalories[0])
print(sum(sortedSumCalories[:3]))

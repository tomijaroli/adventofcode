import string

input = open('input', 'r').read().splitlines()
prioritiesMap = list(string.ascii_letters)

compartmentPairs = [ [ line[:(int(len(line)/2))], line[(int(len(line)/2)):] ]for line in input ]
commonItems = [ ''.join(set(pair[0]).intersection(pair[1])) for pair in compartmentPairs ]
priorities = [ prioritiesMap.index(item) + 1 for item in commonItems ]

print(sum(priorities))

groups = [ input[index:index + 3] for index in range(0, len(input), 3) ]
badges = [ ''.join(set(group[0]).intersection(group[1], group[2])) for group in groups ]
badgePriorities = [ prioritiesMap.index(badge) + 1 for badge in badges ]

print(sum(badgePriorities))

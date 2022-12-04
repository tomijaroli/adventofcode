import re
from collections import Counter

input = open('input', 'r').read().splitlines()
intervals = [ [ int(value) for value in re.split('-|,', line) ] for line in input ]

overlaps = [
    (interval[0] <= interval[2] and interval[1] >= interval[3]) or (interval[0] >= interval[2] and interval[1] <= interval[3])
    for interval in intervals
]
numberOfOverlappingIntervals = Counter(overlaps)[True]
print(numberOfOverlappingIntervals)

overlaps = [
    min(interval[1], interval[3]) - max(interval[0], interval[2]) >= 0
    for interval in intervals
]
numberOfOverlappingIntervals = Counter(overlaps)[True]
print(numberOfOverlappingIntervals)

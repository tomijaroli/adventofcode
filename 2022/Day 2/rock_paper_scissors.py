input = open('input', 'r').read().splitlines()
games = [ line.split(" ") for line in input]

opponentMoveMap = { 'A': 0, 'B': 1, 'C': 2 }
playerMoveMap = { 'X': 0, 'Y': 1, 'Z': 2 }
scoreMap = { 1: 0, 2: 6, 0: 3 }

moves = [ [ opponentMoveMap[game[0]], playerMoveMap[game[1]] ] for game in games ]
scores = [ scoreMap[ (3 + move[0] - move[1]) % 3 ] + move[1] + 1 for move in moves ]
print(sum(scores))

modifiedScoreMap = { 'X': 0, 'Y': 3, 'Z': 6 }
playerMoveBonusMap = {
    'X': { 'A': 3, 'B': 1, 'C': 2 },
    'Y': { 'A': 1, 'B': 2, 'C': 3 },
    'Z': { 'A': 2, 'B': 3, 'C': 1 }
}

scores = [ modifiedScoreMap[game[1]] + playerMoveBonusMap[game[1]][game[0]] for game in games ]
print(sum(scores))

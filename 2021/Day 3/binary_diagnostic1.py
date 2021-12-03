binaries = open('input').readlines()

occurences = [0] * 12

for binary in binaries:
    digits = [char for char in binary.strip()]
    for index, digit in enumerate(digits):
        if digit == '0':
            occurences[index] -= 1
        else:
            occurences[index] += 1

gamma_rate, epsilon_rate = list(list(t) for t in zip(
    *[(int(num > 0), int(num < 0)) for num in occurences])
)

gamma_rate = int(''.join(str(digit) for digit in gamma_rate), 2)
epsilon_rate = int(''.join(str(digit) for digit in epsilon_rate), 2)

print(gamma_rate * epsilon_rate)

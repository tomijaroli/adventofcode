with open('input') as file:
    diagnostics = file.read().splitlines()

line_length = len(diagnostics[0])


def number_of_ones(nums):
    return [sum(num[i] == "1" for num in nums) for i in range(line_length)]


def get_least_common(number, remaining_list_length):
    return int(remaining_list_length / 2 <= number)


def get_most_common(number, remaining_list_length):
    return int(remaining_list_length / 2 > number)


def reduce_list(conditioner):
    remaining = set(diagnostics)
    for i in range(line_length):
        ones = number_of_ones(remaining)
        current = ones[i]
        binary_value_to_match = conditioner(current, len(remaining))

        remaining -= set(number for number in remaining if int(number[i]) != binary_value_to_match)

        if len(remaining) == 1:
            return int(''.join(str(digit) for digit in list(remaining)), 2)


oxigen_generator_rating = reduce_list(get_most_common)
co2_scrubber_rating = reduce_list(get_least_common)

print(oxigen_generator_rating * co2_scrubber_rating)

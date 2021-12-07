input_file = open('input.txt', 'r')
numbers = input_file.readlines()
number_bins = len(numbers[0]) - 1

accumulator = [0] * number_bins
total = 0
for number in numbers:
    for i in range(0, number_bins):
        accumulator[i] += int(number[i])
    total += 1

gamma = int("".join([str(int(amount > total / 2)) for amount in accumulator]), 2)
epsilon = 2**number_bins - gamma - 1

print(f'Gamma:   {gamma}\nEpsilon: {epsilon}\nTotal:   {gamma * epsilon}')

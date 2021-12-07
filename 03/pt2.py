input_file = open('input.txt', 'r')
raw_numbers = input_file.readlines()
number_bins = len(raw_numbers[0]) - 1

numbers = []
for raw_number in raw_numbers:
    number = [int(digit) for digit in raw_number[0:number_bins]]
    numbers.append(number)


def filter_bit(numbers, index, invert=False):
    count = 0
    halves = [[], []]
    for number in numbers:
        count += number[index]
        halves[number[index]].append(number)
    if (count >= 0.5 * len(numbers)) != invert:
        return halves[1]
    else:
        return halves[0]


oxyrating = numbers.copy()
for index in range(0, number_bins):
    oxyrating = filter_bit(oxyrating, index)
    if len(oxyrating) <= 1:
        break
    print(f'index: {index}\nnleft: {len(oxyrating)}')
oxy = int("".join([str(int(bit)) for bit in oxyrating[0]]), 2)


co2rating = numbers.copy()
for index in range(0, number_bins):
    co2rating = filter_bit(co2rating, index, True)
    if len(co2rating) <= 1:
        break
    print(f'index: {index}\nnleft: {len(co2rating)}')
co2 = int("".join([str(int(bit)) for bit in co2rating[0]]), 2)
print(f'Oxy: {oxy}\nCo2: {co2}\nsup: {oxy * co2}')



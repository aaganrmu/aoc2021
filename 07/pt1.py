input_file = open('input.txt', 'r')
raw_data = input_file.readlines()
raw_crabs = raw_data[0].split(',')

crabs = [int(raw_crab) for raw_crab in raw_crabs]

# "A group of crabs is called a ‘cast’."
# https://www.mba.ac.uk/fact-sheet-crabs

cast = [0] * (max(crabs) + 1)

for crab in crabs:
    cast[crab] += 1


def fuel_used_to_travel_to_position(cast, position):
    fuel = 0
    for height in range(0, len(cast)):
        fuel += cast[height] * abs(height - position)
    return fuel


best_fuel_use = 999999
for height in range(0, len(cast)):
    fuel_used = fuel_used_to_travel_to_position(cast, height)
    best_fuel_use = min(fuel_used, best_fuel_use)

print(best_fuel_use)


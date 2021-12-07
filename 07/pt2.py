input_file = open('input.txt', 'r')
raw_data = input_file.readlines()
raw_crabs = raw_data[0].split(',')

crabs = [int(raw_crab) for raw_crab in raw_crabs]

# "A group of crabs is called a ‘cast’."
# https://www.mba.ac.uk/fact-sheet-crabs

cast = [0] * (max(crabs) + 1)

for crab in crabs:
    cast[crab] += 1


def fuel_cost(distance):
    return 0.5 * (distance ** 2 + distance)


def fuel_used_to_travel_to_position(cast, position):
    fuel = 0
    for height in range(0, len(cast)):
        fuel += cast[height] * fuel_cost(abs(height - position))
    return fuel


best_fuel_use = 99999999999
for height in range(0, len(cast)):
    fuel_used = fuel_used_to_travel_to_position(cast, height)
    best_fuel_use = min(fuel_used, best_fuel_use)

print(int(best_fuel_use))

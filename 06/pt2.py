input_file = open('input.txt', 'r')
raw_data = input_file.readlines()
fishes = raw_data[0].split(',')

# Calculate amount of fish for each timer
# This uses a different representation.
# The example 3,4,3,1,2 would become
# [0, 1, 1, 2, 1, 0, 0, 0, 0].
school = [0] * 9
for fish in fishes:
    school[int(fish)] += 1

def advance_day(school):
    growth = school.pop(0)
    school[6] += growth
    school.append(growth)
    return school

for day in range(0,256):
    advance_day(school)


print(sum(school))



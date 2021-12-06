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
    # element 0 of list are all fish that are due to pop out a baby
    # pop(0) also shifts all other fish one place left, i.e. decrease their timers
    growth = school.pop(0)
    # all those ex-preggers fish have their timer reset to 6
    school[6] += growth
    # all baby fish have their their timer set to 8.
    # due to pop(0) there is no element 8 anymore so we append it.
    school.append(growth)
    return school


for day in range(0, 80):
    advance_day(school)


print(sum(school))

import numpy

input_file = open('input.txt', 'r')
commands = input_file.readlines()

position = numpy.array([0, 0])
directions = {
    'forward': numpy.array([1, 0]),
    'up': numpy.array([0, 1]),
    'down': numpy.array([0, -1])
}

for command in commands:
    direction = command.split(' ')[0]
    distance = int(command.split(' ')[1])
    move = directions[direction] * distance
    position = position + move

print(position)
print(position[0] * position[1])

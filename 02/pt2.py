input_file = open('input.txt', 'r')
commands = input_file.readlines()

aim = 0
x = 0
depth = 0


for command in commands:
    direction = command.split(' ')[0]
    magnitude = int(command.split(' ')[1])
    if (direction == 'up'):
        aim = aim - magnitude
    if (direction == 'down'):
        aim = aim + magnitude
    if (direction == 'forward'):
        x = x + magnitude
        depth = depth + magnitude * aim

print(f'{x} {depth}')
print(x * depth)

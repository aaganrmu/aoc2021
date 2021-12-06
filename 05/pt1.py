input_file = open('input.txt', 'r')
vents_raw = input_file.readlines()
MAX_X = MAX_Y = 1000


class Position:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def read_raw_position(self, position_raw: str):
        [self.x, self.y] = [int(n) for n in position_raw.split(',')]


class Vent:
    def __init__(self, raw_vent: str = None):
        self.start = Position()
        self.end = Position()
        if raw_vent is not None:
            self.read_raw_vent(raw_vent)

    def read_raw_vent(self, vent_raw: str):
        [start_raw, end_raw] = vent_raw.split(' -> ')
        self.start.read_raw_position(start_raw)
        self.end.read_raw_position(end_raw)

    def is_horizontal(self):
        return self.start.y == self.end.y

    def is_vertical(self):
        return self.start.x == self.end.x

    # returns list of positions where this vent is
    def map_positions(self):
        if self.is_horizontal():
            if self.start.x < self.end.x:
                xes = range(self.start.x, self.end.x + 1)
            else:
                xes = range(self.end.x, self.start.x + 1)
            return [Position(x, self.start.y) for x in xes]
        if self.is_vertical():
            if self.start.y < self.end.y:
                ys = range(self.start.y, self.end.y + 1)
            else:
                ys = range(self.end.y, self.start.y + 1)
            return [Position(self.start.x, y) for y in ys]

    def __str__(self):
        return(f'{self.start.x}, {self.start.y}, {self.end.x}, {self.end.y}')


# Process raw input
vents = []
for vent_raw in vents_raw:
    vent = Vent(vent_raw)
    if (vent.is_vertical() or vent.is_horizontal()):
        vents.append(vent)

# Draw on the grid
vent_map = [[0 for y in range(0, MAX_X)] for x in range(0, MAX_Y)]
for vent in vents:
    for position in vent.map_positions():
        vent_map[position.x][position.y] += 1


# for y in range(0, MAX_Y):
#     print(''.join([str(vent_map[x][y]) for x in range(0, MAX_X)]))

peaks = 0
for x in range(0, MAX_X):
    for y in range(0, MAX_Y):
        if vent_map[x][y] > 1:
            peaks += 1

print(peaks)

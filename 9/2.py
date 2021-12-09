import collections


def read_input(filename):
    with open(filename) as f:
        return [l.strip() for l in f.readlines() if l.strip() != '']


def get_adjacents(floor, x, y):
    valid_adjacents = []

    if x > 0:
        up = floor[x - 1][y]
        if up >= 0 and up < 9:
            floor[x - 1][y] = -1
            valid_adjacents.append((x - 1, y, up))

    if x < len(floor[0]) - 1:
        down = floor[x + 1][y]
        if down >= 0 and down < 9:
            floor[x + 1][y] = -1
            valid_adjacents.append((x + 1, y, down))

    if y > 0:
        left = floor[x][y - 1]
        if left >= 0 and left < 9:
            floor[x][y - 1] = -1
            valid_adjacents.append((x, y - 1, left))

    if y < len(floor) - 1:
        right = floor[x][y + 1]
        if right >= 0 and right < 9:
            floor[x][y + 1] = -1
            valid_adjacents.append((x, y + 1, right))

    return (floor, valid_adjacents)
    # returns [(x, y, value)]


def main():
    input = read_input('input.txt')

    floor = []

    for line in input:
        x = []
        for char in line:
            x.append(int(char))

        floor.append(x)

    lowests = []

    for x, row in enumerate(floor):
        for y, cell in enumerate(row):
            up = 9999
            down = 9999
            left = 9999
            right = 9999

            if x > 0:
                up = floor[x - 1][y]

            if x < len(row) - 1:
                down = floor[x + 1][y]

            if y > 0:
                left = floor[x][y - 1]

            if y < len(floor) - 1:
                right = floor[x][y + 1]

            if cell < up and cell < down and cell < left and cell < right:
                lowests.append((x, y, cell))
    updated_floor = floor

    basins = []
    basin_sizes = []
    for lowest in lowests:
        queue = [lowest]
        basin_size = 0
        basin_cells = []
        while queue:
            x1, y1, cell = queue.pop()
            basin_cells.append((x1, y1, cell))
            basin_size += 1
            updated_floor, adjacents = get_adjacents(updated_floor, x1, y1)
            queue.extend(adjacents)
        basins.append(basin_cells)
        basin_sizes.append(basin_size - 1)  # not sure why off by 1?

    basin_sizes.sort()
    for row in updated_floor:
        line_str = ['x' if cell == -1 else str(cell) for cell in row]
        print(''.join(line_str))
    print(basin_sizes)
    print(basin_sizes[-3:])
    print(106 * 111 * 112)


if __name__ == '__main__':
    main()

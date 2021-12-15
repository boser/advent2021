import collections
from os import X_OK


def read_input(filename):
    with open(filename) as f:
        return [l.strip() for l in f.readlines() if l.strip() != '']


def main():
    input = read_input('input.txt')

    folds = []
    coordinates = []
    for line in input:
        
        if 'fold along' in line:
            folds.append(line)
        else:
            [x, y] = line.split(',')

            int_x = int(x)
            int_y = int(y)
            coordinates.append((int_x, int_y))
    
    print('coords', len(coordinates))
    updated_coordinates = set(coordinates)

    for fold in folds[0:13]:
        fold_line = fold.split(' ')[-1]
        [fold_direction, axis] = fold_line.split('=')

        axis = int(axis)
        new_coordinates = set()
        if fold_direction == 'x':
            for (x, y) in updated_coordinates:
                if x > axis:
                    new_x = axis*2 - x
                    new_coordinates.add((new_x, y))
                else:
                    new_coordinates.add((x, y))
        else:
            for (x, y) in updated_coordinates:
                if y > axis:
                    new_y = axis*2 - y
                    new_coordinates.add((x, new_y))
                else:
                    new_coordinates.add((x, y))
        updated_coordinates = set(new_coordinates)

    print(updated_coordinates)
    # matrix = [['0'] * 1000] * 1000
    max_x = 0
    max_y = 0
    for (x, y) in updated_coordinates:
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y

    print(max_x, max_y)
    matrix = [[
        '.' for col in range(max_x+ 1)
    ] for row in range(max_y+ 1)]


    for (x, y) in updated_coordinates:
        print('x', x, y)
        matrix[y][x] = '#'

    for line in matrix:
        print(''.join(line))


if __name__ == '__main__':
    main()

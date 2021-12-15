import copy

from os import X_OK


def read_input(filename):
    with open(filename) as f:
        return [l.strip() for l in f.readlines() if l.strip() != '']

def flash(x, y, grid):
    new_grid = copy.deepcopy(grid)
    if x > 0:
        new_grid[x-1][y] += 1
    if x < len(grid) - 1:
        new_grid[x+1][y] += 1
    if y > 0:
        new_grid[x][y-1] += 1
    if y < len(grid[0]) - 1:
        new_grid[x][y+1] += 1


    if x > 0 and y > 0:
        new_grid[x-1][y-1] += 1
    if x < len(grid) -1 and y < len(grid[0]) - 1:
        new_grid[x+1][y+1] += 1

    if x > 0 and y < len(grid[0]) - 1:
        new_grid[x-1][y+1] += 1
    if x < len(grid) - 1 and y > 0:
        new_grid[x+1][y-1] += 1
    
    return new_grid

def check_grid(grid, flashed, flashes_q):
    flashes = []
    for (x,line) in enumerate(grid):
        for (y,cell) in enumerate(line):
            if grid[x][y] > 9 and (x,y) not in flashed and (x,y) not in flashes_q:
                flashes.append((x,y))
    return flashes

def cooldown(grid):
    new_grid = copy.deepcopy(grid)
    for (x,line) in enumerate(new_grid):
        for (y,cell) in enumerate(line):

            if grid[x][y] > 9:
                new_grid[x][y] = 0
    return new_grid

def check_sync(grid):
    sync_num = grid[0][0]
    for line in grid:
        for cell in line:
            if cell != sync_num:
                return False

    return True

def main():
    input = read_input('input.txt')

    grid = []
    flashes_q = []
    for line in input:
        l = []
        for char in line:
            l.append(int(char))
        grid.append(l)

    flashes_count = 0
    for step in range(9999):
        flashes_q = []
        flashed = set()

        for (x,line) in enumerate(grid):
            for (y,cell) in enumerate(line):
                grid[x][y] += 1

        flashes_q.extend(check_grid(grid, flashed, flashes_q))

        while flashes_q:
            (x,y) = flashes_q.pop(0)
            flashed.add((x,y))
            grid = flash(x, y, grid)
            flashes_count += 1
            flashes = check_grid(grid, flashed, flashes_q)
            if flashes:
                flashes_q.extend(flashes)

        
        grid = cooldown(grid)

        if check_sync(grid):
            print('SYNC FOUND', step)
            for line in grid:
                print(line)
            return
    
        for line in grid:
            print(line)
        print('----')


    print(flashes_count)
if __name__ == '__main__':
    main()

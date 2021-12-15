import copy

from os import X_OK


def read_input(filename):
    with open(filename) as f:
        return [l.strip() for l in f.readlines() if l.strip() != '']

# current path is list of nodes reached until now
# part 2 is probably cycle detection

def visit(path_so_far, current, map):
    updated_path_so_far = copy.deepcopy(path_so_far)
    updated_path_so_far.append(current)
    if current == 'end':
        return [updated_path_so_far]
    else:
        paths = []
        for next in map[current]:
            if next in map:
                if current.isupper() or current not in path_so_far:
                    paths += visit(updated_path_so_far, next, map)
        return paths

def main():
    input = read_input('input.txt')

    map = {}
    

    for line in input:
        nodes = line.split('-')
        start = nodes[0]
        end = nodes[1]
        
        if start in map:
            map[start].append(end)
        else:
            map[start] = [end]
        if end in map:
            map[end].append(start)
        else:
            map[end] = [start]

    paths = visit([], 'start', map)
    print(len(paths))



if __name__ == '__main__':
    main()

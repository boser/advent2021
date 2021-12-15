import copy
import collections
from os import X_OK


def read_input(filename):
    with open(filename) as f:
        return [l.strip() for l in f.readlines() if l.strip() != '']

def main():
    input = read_input('input.txt')

    map = {}
    
    start_string = input[0]
    map = {}
    for line in input[1:]:
        tokens = line.split(' -> ')
        start = tokens[0]
        end = tokens[1]

        map[start] = end

    print(map)

    updated_string = start_string
    # print(updated_string)
    for i in range(10):
        print(i)
        buffer = ''
        next_string = ''
        for i in updated_string:
            buffer = buffer + i
            buffer = buffer[-2:]

            if buffer in map:
                next_string += buffer[0] + map[buffer]
        next_string += i

        updated_string = next_string

    # print(updated_string)
    char_map = collections.defaultdict(int)
    for i in updated_string:
        char_map[i] += 1

    v = list(char_map.values())
    v.sort()
    print(char_map)
    print(v)
    print(v[-1] - v[0])

if __name__ == '__main__':
    main()

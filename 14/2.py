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
    map = {} # the next two pairs off of each pair
    char_insert = {} # the character that gets inserted
    map_state = {} # the state of pairs
    for line in input[1:]:
        # create token map
        tokens = line.split(' -> ')
        start = tokens[0]
        end = tokens[1]

        tok1 = start[0] + end
        tok2 = end + start[1]
        map[start] = [tok1, tok2]
        char_insert[start] = end
        map_state[start] = 0
    
    buffer = ''
    freq_list = collections.defaultdict(int) # frequency list
    for i in start_string:
        buffer = buffer + i
        buffer = buffer[-2:]

        if buffer in map_state:
            map_state[buffer] += 1
        freq_list[i] += 1

    updated_map_state = copy.deepcopy(map_state)    # CURRENT PAIRS
    for i in range(40):
        next_map_state = collections.defaultdict(int)
        for key in updated_map_state:
            # each pair generates 2 more pairs
            next_map_state[map[key][0]] += updated_map_state[key]
            next_map_state[map[key][1]] += updated_map_state[key]

            insert_letter = char_insert[key]

            # and each pair generates 1 more letter
            freq_list[insert_letter] += updated_map_state[key]

        updated_map_state = next_map_state

    # so use a pair freq list to generate the next pairs
    # and each pair inserts into a char frequency list

    print(updated_map_state)
    print(freq_list)
    v = list(freq_list.values())
    v.sort()
    print('v', v)
    print(v[-1] - v[0])
if __name__ == '__main__':
    main()

import collections

def read_input(filename):
    with open(filename) as f:
        return [l.strip() for l in f.readlines() if l.strip() != '']

signal_map = {
    0: 6,
    1: 2,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6
}

def main():
    input = read_input('input.txt')
    
    buckets = collections.defaultdict(int)

    for line in input:
        line_sp = line.split('|')
        digits = line_sp[1].split(' ')

        for digit in digits:
            buckets[len(digit)] += 1
    print('buckets', buckets)
    print('buckets', buckets[signal_map[1]] + buckets[signal_map[4]] + buckets[signal_map[7]] + buckets[signal_map[8]])

if __name__ == '__main__':
    main()

import collections


def read_input(filename):
    with open(filename) as f:
        return [l.strip() for l in f.readlines() if l.strip() != '']


def main():
    input = read_input('input.txt')

    openers = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>',
    }
    closers = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }

    bads = {
        ')': 0,
        ']': 0,
        '}': 0,
        '>': 0,
    }
    for line in input:
        line_stack = []
        for char in line:
            if char in openers:
                line_stack.append(char)
            elif char in closers:
                if openers[line_stack[-1]] != char:
                    bads[char] += 1
                    break
                else:
                    line_stack.pop()

    print(bads)
    score = 0
    for char, bad in bads.items():
        score += closers[char] * bad
    print(score)


if __name__ == '__main__':
    main()

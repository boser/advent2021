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
    incomplete_lines = []
    incomplete_remainders = []
    for line in input:
        line_stack = []
        for char in line:
            if char in openers:
                line_stack.append(char)
            elif char in closers:
                if openers[line_stack[-1]] != char:
                    bads[char] += 1
                    line_stack = []
                    break
                else:
                    line_stack.pop()
            # dont evaluate

        incomplete_lines.append(line)
        if line_stack:
            incomplete_remainders.append(line_stack)

    char_map = {
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4,
    }
    scores = []
    for incomplete in incomplete_remainders:
        score = 0
        rev_incomplete = reversed(incomplete)
        for char in rev_incomplete:
            score = score * 5 + char_map[char]
        scores.append(score)

    print(scores)
    scores.sort()
    print(scores)
    print(len(scores))
    print(scores[int(len(scores) / 2)])
    # print(bads)
    # score = 0
    # for char, bad in bads.items():
    #     score += closers[char] * bad
    # print(score)


if __name__ == '__main__':
    main()

import collections


def read_input(filename):
    with open(filename) as f:
        return [l.strip() for l in f.readlines() if l.strip() != '']


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
                lowests.append(cell)

    print(lowests)
    score = sum(lowests) + len(lowests)
    print(score)


if __name__ == '__main__':
    main()

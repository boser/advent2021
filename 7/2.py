def read_input(filename):
    with open(filename) as f:
        return [l.strip() for l in f.readlines() if l.strip() != '']


def main():
    input = read_input('input.txt')

    start_str = input[0].split(',')
    start = [int(f) for f in start_str]

    least_fuel_pos = 0
    least_fuel = 99999999999
    for i in range(1000):
        fuel = 0
        for position in start:
            n = abs(position - i)
            fuel_tri = (n * (n + 1)) / 2
            fuel += fuel_tri
        if fuel < least_fuel:
            least_fuel = fuel
            least_fuel_pos = i

    print(least_fuel_pos, least_fuel)


if __name__ == '__main__':
    main()

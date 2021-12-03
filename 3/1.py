def read_input(filename):
    with open(filename) as f:
        return [l.strip() for l in f.readlines() if l.strip() != '']



def main():
    input = read_input('input.txt')

    bits = []

    for idx, init in enumerate(input[0]):
        if len(bits) <= idx:
            bits.append(0)

    for line in input:
        for idx, char in enumerate(line):
            bits[idx] += int(char)

    print(bits)
    gamma = ''.join(list(map(lambda bit: '1' if bit > 500 else '0', bits)))
    epsilon = ''.join(list(map(lambda bit: '0' if bit > 500 else '1', bits)))

    print('gamma', gamma,  int(gamma,2))
    print('epsilon', epsilon, int(epsilon,2))
    print(int(gamma,2)*int(epsilon,2))

if __name__ == '__main__':
    main()

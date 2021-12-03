def read_input(filename):
    with open(filename) as f:
        return [l.strip() for l in f.readlines() if l.strip() != '']


def get_most_common_bit_at_index(idx, input):
    half = len(input) / 2

    bit_count = 0
    for line in input:
        bit_count += int(line[idx])

    if bit_count == half:
        return -1
    else:
        return 1 if bit_count > half else 0

def main():
    input = read_input('input.txt')

    str_size = len(input[0])

    ox_input = input
    co_input = input
    for idx in range(str_size):
        ox_common_bit = get_most_common_bit_at_index(idx, ox_input)
        # print('most common ox bit at index', idx, ox_common_bit)
        if len(ox_input) > 1:
            if ox_common_bit == -1 or ox_common_bit == 1:
                ox_input = list(filter(lambda input: True if input[idx] == '1' else False, ox_input))
            else:
                ox_input = list(filter(lambda input: True if input[idx] == '0' else False, ox_input))

        co_common_bit = get_most_common_bit_at_index(idx, co_input)
        # print('most common co bit at index', idx, co_common_bit)

        if len(co_input) > 1:
            if co_common_bit == -1 or co_common_bit == 1:
                co_input = list(filter(lambda input: True if input[idx] == '0' else False, co_input))
            else:
                co_input = list(filter(lambda input: True if input[idx] == '1' else False, co_input))

        # print(ox_input)   
        # print(co_input)   

    ox_input = ox_input[0]
    co_input = co_input[0]

    print(ox_input)   
    print(co_input)   
    print(int(co_input, 2),int(ox_input, 2), int(ox_input, 2) * int(co_input, 2))

    
    # for idx in range(str_size):


    # print(get_most_common_bit_at_index(0, input))
    # bits = []

    # for idx, init in enumerate(input[0]):
    #     if len(bits) <= idx:
    #         bits.append(0)

    # for line in input:
    #     for idx, char in enumerate(line):
    #         bits[idx] += int(char)

    # print(bits)
    # gamma = ''.join(list(map(lambda bit: '1' if bit > 500 else '0', bits)))
    # epsilon = ''.join(list(map(lambda bit: '0' if bit > 500 else '1', bits)))

    # print('gamma', gamma,  int(gamma,2))
    # print('epsilon', epsilon, int(epsilon,2))
    # print(int(gamma,2)*int(epsilon,2))

if __name__ == '__main__':
    main()

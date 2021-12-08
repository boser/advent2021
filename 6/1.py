
def read_input(filename):
    with open(filename) as f:
        return [l.strip() for l in f.readlines() if l.strip() != '']



def main():
    input = read_input('input.txt')

    start_str = input[0].split(',')
    start = [int(f) for f in start_str]

    for i in range(80):
        end = []
        for fish in start:
            if fish == 0:
                end.append(6)
                end.append(8)
            else:
                end.append(fish-1)
        start = end
    
    print(len(end))

if __name__ == '__main__':
    main()

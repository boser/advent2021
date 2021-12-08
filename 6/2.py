
def read_input(filename):
    with open(filename) as f:
        return [l.strip() for l in f.readlines() if l.strip() != '']



def main():
    input = read_input('input.txt')

    start_str = input[0].split(',')
    start = [int(f) for f in start_str]


    buckets = [0,0,0,0,0,0,0,0,0]
    next_buckets = [0,0,0,0,0,0,0,0,0]

    for s in start:
        buckets[s] += 1

    print('start', buckets)

    for i in range(256):
        print('buckets', buckets, buckets[0])
        next_buckets[0] = buckets[1]
        next_buckets[1] = buckets[2]
        next_buckets[2] = buckets[3]
        next_buckets[3] = buckets[4]
        next_buckets[4] = buckets[5]
        next_buckets[5] = buckets[6]
        next_buckets[6] = buckets[7] + int(buckets[0])
        next_buckets[7] = buckets[8]
        next_buckets[8] = int(buckets[0])
        print(next_buckets)
        buckets = [b for b in next_buckets]
    print(sum(next_buckets))
    # for i in range(80):
    #     end = []
    #     for fish in start:
    #         if fish == 0:
    #             end.append(6)
    #             end.append(8)
    #         else:
    #             end.append(fish-1)
    #     start = end
    
    # print(len(end))

if __name__ == '__main__':
    main()

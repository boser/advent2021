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

    
def intersection(a, b):
    return list(set(a) & set(b))

def main():
    input = read_input('input.txt')
    
    buckets = collections.defaultdict(int)
    answers = []
    for line in input:
        buckets = collections.defaultdict(int)
        line_sp = line.split(' | ')
        signal = line_sp[0].split(' ')
        digits = line_sp[1].split(' ')

        entries = signal + digits

        solve = {}

        # EVERY LINE HAS 1 4 7 8
        # these we know for sure
        for entry in entries:
            sorted_entry = sorted(entry)
            if len(sorted_entry) == 2:
                solve[1] = sorted_entry
            elif len(sorted_entry) == 4:
                solve[4] = sorted_entry
            elif len(sorted_entry) == 3:
                solve[7] = sorted_entry
            elif len(sorted_entry) == 7:
                solve[8] = sorted_entry

        # these we can deduce off of 1478
        print('solve is', solve)
        for entry in entries:
            sorted_entry = sorted(entry)
            if len(sorted_entry) == 5:
                # we know we have 2 3 or 5
                common_with_one = intersection(sorted_entry, solve[1])
                if len(common_with_one) == 2:
                    solve[3] = sorted_entry
                else:
                    common_with_four = intersection(sorted_entry, solve[4])
                    if len(common_with_four) == 3:
                        solve[5] = sorted_entry
                    else:
                        solve[2] = sorted_entry

            elif len(sorted_entry) == 6:
                common_with_four = intersection(sorted_entry, solve[4])
                if len(common_with_four) == 4:
                    solve[9] = sorted_entry
                else:
                    common_with_one = intersection(sorted_entry, solve[1])
                    if len(common_with_one) == 2:
                        solve[0] = sorted_entry
                    else:
                        solve[6] = sorted_entry
        
        # solve has everything now
        key = {}
        for k, v in solve.items():
            s = ''.join(v)
            key[s] = k

        solved_digits = []
        for digit in digits:
            sorted_digit = ''.join(sorted(digit))
            solved_digits.append(str(key[sorted_digit]))

        answers.append(int(''.join(solved_digits)))

    print('answers', answers)
    print('answers', sum(answers))

    # b   a
    # b   a
    #  eee
    #     f
    #     f

    # for sig in signal:
    #     buckets[len(sig)] += 1
    # for dig in digits:
    #     buckets[len(dig)] += 1

    # entries = signal + digits

    # print(entries)
    
    # commons:
    # len 2 = 1
    # len 4 = 4
    # len 3 = 7
    # len 7 = 8

    # len 5 = 2,3,5
        # if all of 1 belongs, then it is 3
        # else it is 2 or 5
            # if intersect with 4 = 3, it is 5
            # else 2

    # len 6 = 0,6,9
        # contains all of 4 = 9
        # 
        # 0 contains all of 1 and is not 9
        # 6 is the last one
        #         

if __name__ == '__main__':
    main()

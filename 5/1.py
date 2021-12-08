
def read_input(filename):
    with open(filename) as f:
        return [l.strip() for l in f.readlines() if l.strip() != '']



def main():
    board = [
        [
            0 for j in range(1000)
        ]
        for i in range(1000)
    ]

    input = read_input('input.txt')
    for line in input:
        coordinates = line.split(' -> ')
        start = coordinates[0].split(',')
        end = coordinates[1].split(',')

        x1 = int(start[0])
        y1 = int(start[1])

        x2 = int(end[0])
        y2 = int(end[1])


        # # increase for simplicity
        if x1 == x2:
            if y1 <= y2:
                print('horizontal @ ', x1, ': ', y1, ' to ' , y2)
                for i in range(y1,y2+1):
                    board[x1][i] += 1
            else: 
                print('horizontal @ ', x1, ': ', y2, ' to ' , y1)
                for i in range(y2,y1+1):
                    board[x1][i] += 1

        elif y1 == y2:
            if x1 <= x2:
                
                print('vertical @ ', y1, ': ', x1, ' to ' , x2)
                for i in range(x1,x2+1):
                    board[i][y1] += 1
            else: 
                print('vertical @ ', y1, ': ', x2, ' to ' , x1)
                for i in range(x2,x1+1):
                    board[i][y1] += 1

    danger_count = 0

    for row in board:
        for cell in row:
            if cell >= 2:
                danger_count+=1

    print(danger_count)


if __name__ == '__main__':
    main()

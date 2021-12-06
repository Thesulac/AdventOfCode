def board_sum(board):
    return sum([sum(filter(None, l)) for l in board])


def part1():
    data = open('input').read().split('\n\n')

    nums = list(map(int, data[0].split(',')))
    boards = [[list(map(int, l.split())) for l in board.split('\n')] for board in data[1:]]

    for num in nums:
        for board in boards:
            for l in board:
                if num in l:
                  l[l.index(num)] = None

        for board in boards:
          for i in range(len(board[0])):
              if all(l[i] is None for l in board) or all(j is None for j in board[i]):
                print("part 1 : ", board_sum(board) * num)
                return


def part2():
    data = open('input').read().split('\n\n')

    nums = list(map(int, data[0].split(',')))
    boards = [[list(map(int, l.split())) for l in board.split('\n')] for board in data[1:]]

    score = []
    for num in nums:
        for board in boards:
            for l in board:
                if num in l:
                  l[l.index(num)] = None

        for board in boards:
            for i in range(len(board[0])):
              if all(l[i] is None for l in board) or all(j is None for j in board[i]):
                score.append(board_sum(board)*num)
                if board in boards:
                  boards.remove(board)

    print("part 2 : ", score[-1])


if __name__ == "__main__":

    part1()
    part2()
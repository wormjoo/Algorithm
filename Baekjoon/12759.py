def check_win(board, player):
    win_conf = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
        ]
    return [player, player, player] in win_conf

def who_win(board):
    if check_win(board, 1):
        print(1)
    elif check_win(board, 2):
        print(2)
    else:
        print(0)

board = [[0]*3 for i in range(3)]
cnt = 1
player = int(input())


while True:
    if cnt > 9:
        break
    x, y = map(int, input().split())
    board[x-1][y-1] = player

    if check_win(board, player):
        break
    
    if player == 1:
        player = 2
    else:
        player = 1
    cnt += 1

who_win(board)

# W01 Prove Developer
# Author: Alec Mateski

def write_board(board):
    print(f'{board[0]}|{board[1]}|{board[2]}\n-+-+-\n{board[3]}|{board[4]}|{board[5]}\n-+-+-\n{board[6]}|{board[7]}|{board[8]}')
    return 0

def board_assign(input, board, player_turn):
    board[input - 1] = player_turn
    return 0

def take_turn(player_turn, board):
    input_check = 0
    while input_check == 0:
        board_number = input(f'{player_turn}\'s turn to choose a square (1-9): ')
        if int(board_number) > 9 or int(board_number) < 1:
            print('Please choose a valid board position.\n')
        elif board[int(board_number) - 1] == 'x' or board[int(board_number) - 1] == 'o':
            print('Space taken, please select a valid board position.\n')
        else:
            input_check = 1
    board_assign(int(board_number), board, player_turn)
    return 0

def check_victory(board):
    game_state = 0
    
    return game_state

def main():
    #establish board
    game = 0
    turn = 1
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    player_turn = 'x'
    while game == 0 and turn < 9:
        write_board(board)
        take_turn(player_turn, board)
        if player_turn == 'x':
            player_turn = 'o'
        else:
            player_turn = 'x'
        turn += 1
        check_victory(board)
    return 0

main()
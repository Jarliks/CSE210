# W01 Prove Developer
# Tic-tac-toe!
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
    #horizontal top
    if board[0] == board[1] and board[1] == board[2]:
        winner = board[0]
        game_state = 1
        write_board(board)
        print(f'Winner is {winner}, good game!')
    #horizontal mid
    elif board[3] == board[4] and board[4] == board[5]:
        winner = board[3]
        game_state = 1
        write_board(board)
        print(f'Winner is {winner}, good game!')
    #horizontal mid
    elif board[6] == board[7] and board[7] == board[8]:
        winner = board[6]
        game_state = 1
        write_board(board)
        print(f'Winner is {winner}, good game!')
    #vertical left
    elif board[0] == board[3] and board[3] == board[6]:
        winner = board[0]
        game_state = 1
        write_board(board)
        print(f'Winner is {winner}, good game!')
    #vertical mid
    elif board[1] == board[4] and board[4] == board[7]:
        winner = board[1]
        game_state = 1
        write_board(board)
        print(f'Winner is {winner}, good game!')
    #vertical right
    elif board[2] == board[5] and board[5] == board[8]:
        winner = board[2]
        game_state = 1
        write_board(board)
        print(f'Winner is {winner}, good game!')
    #diagonal top left to bottom right
    elif board[0] == board[4] and board[4] == board[8]:
        winner = board[0]
        game_state = 1
        write_board(board)
        print(f'Winner is {winner}, good game!')
    #diagonal top right to bottom left
    elif board[2] == board[4] and board[4] == board[6]:
        winner = board[2]
        game_state = 1
        write_board(board)
        print(f'Winner is {winner}, good game!')
    
    return game_state

def main():
    #establish board
    game = 0
    turn = 0
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    player_turn = 'x'
    while game == 0:
        write_board(board)
        take_turn(player_turn, board)
        if player_turn == 'x':
            player_turn = 'o'
        else:
            player_turn = 'x'
        turn += 1
        game = check_victory(board)
        if game == 0 and turn == 9:
            write_board(board)
            print('Cat\'s game, its a draw!')
            game = 1
    return 0

main()
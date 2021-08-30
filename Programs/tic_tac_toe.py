import random

game_board = {
    'top-L': ' ',
    'top-M': ' ',
    'top-R': ' ',
    'mid-L': ' ',
    'mid-M': ' ',
    'mid-R': ' ',
    'bot-L': ' ',
    'bot-M': ' ',
    'bot-R': ' '
}

def print_gameboard(game_board):
    print(game_board['top-L'] + '|' + game_board['top-M'] + '|' + game_board['top-R'])
    print('-+-+-')
    print(game_board['mid-L'] + '|' + game_board['mid-M'] + '|' + game_board['mid-R'])
    print('-+-+-')
    print(game_board['bot-L'] + '|' + game_board['bot-M'] + '|' + game_board['bot-R'])



turn = 'X'

for play in range(9):
    print_gameboard(game_board)
    
    if (game_board['top-L'] == 'X' and game_board['top-M'] == 'X' and game_board['top-R'] == 'X') or \
       (game_board['mid-L'] == 'X' and game_board['mid-M'] == 'X' and game_board['mid-R'] == 'X') or \
       (game_board['bot-L'] == 'X' and game_board['bot-M'] == 'X' and game_board['bot-R'] == 'X') or \
       (game_board['top-L'] == 'X' and game_board['mid-L'] == 'X' and game_board['bot-L'] == 'X') or \
       (game_board['top-M'] == 'X' and game_board['mid-M'] == 'X' and game_board['bot-M'] == 'X') or \
       (game_board['top-R'] == 'X' and game_board['mid-R'] == 'X' and game_board['bot-R'] == 'X') or \
       (game_board['top-L'] == 'X' and game_board['mid-M'] == 'X' and game_board['bot-R'] == 'X') or \
       (game_board['top-R'] == 'X' and game_board['mid-M'] == 'X' and game_board['bot-L'] == 'X'):
        print('Congratualations! You beat the computer!')
        break
    elif (game_board['top-L'] == 'O' and game_board['top-M'] == 'O' and game_board['top-R'] == 'O') or \
       (game_board['mid-L'] == 'O' and game_board['mid-M'] == 'O' and game_board['mid-R'] == 'O') or \
       (game_board['bot-L'] == 'O' and game_board['bot-M'] == 'O' and game_board['bot-R'] == 'O') or \
       (game_board['top-L'] == 'O' and game_board['mid-L'] == 'O' and game_board['bot-L'] == 'O') or \
       (game_board['top-M'] == 'O' and game_board['mid-M'] == 'O' and game_board['bot-M'] == 'O') or \
       (game_board['top-R'] == 'O' and game_board['mid-R'] == 'O' and game_board['bot-R'] == 'O') or \
       (game_board['top-L'] == 'O' and game_board['mid-M'] == 'O' and game_board['bot-R'] == 'O') or \
       (game_board['top-R'] == 'O' and game_board['mid-M'] == 'O' and game_board['bot-L'] == 'O'):
        print('You lost to the computer. Better luck next time!')
        break
    
    else:
    
        print(f'It is the move for {turn}. Type the space: top-L, top-M, top-R, mid-L, mid-M, mid-R, bot-L, bot-M, bot-R')
     
    
        if turn == 'X':
            mark = input()
            game_board[mark] = turn
            turn = 'O'
        else:
            available = []
            for key in game_board:
                if game_board[key] == ' ':
                    available.append(key)
            comp = random.choice(available)
            game_board[comp] = turn
            turn = 'X'
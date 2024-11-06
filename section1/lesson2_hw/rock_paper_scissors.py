input_player1 = input('Player #1, your turn (rock, paper, scissors): ')
input_player2 = input('Player #2, your turn (rock, paper, scissors): ')

if input_player1 == input_player2:
    print('Draw')
elif input_player1 == 'rock' and input_player2 == 'paper':
    print('Player #2 won')
elif input_player1 == 'rock' and input_player2 == 'scissors':
    print('Player #1 won')
elif input_player1 == 'paper' and input_player2 == 'rock':
    print('Player #1 won')
elif input_player1 == 'paper' and input_player2 == 'scissors':
    print('Player #2 won')
elif input_player1 == 'scissors' and input_player2 == 'rock':
    print('Player #2 won')
elif input_player1 == 'scissors' and input_player2 == 'paper':
    print('Player #1 won')
else:
    print('Wrong input, enter from possible ones')

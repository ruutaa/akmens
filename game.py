human_turn = 'rock'
computer_turn = 'rock'

if human_turn == computer_turn:
    print('draw')
elif human_turn == 'rock' and computer_turn == 'scissors':
    print('human wins!!')
elif human_turn == 'paper' and computer_turn == 'rock':
    print('human wins!!')
elif human_turn == 'scissors' and computer_turn == 'paper':
    print('human wins!!') 
elif human_turn == 'rock' and computer_turn == 'paper':
    print('human wins!!')
elif human_turn == 'paper' and computer_turn == 'scissors':
    print('human wins!!')
else:
    print('computer wins!')

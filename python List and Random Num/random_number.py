import random

random_number = random.randint(1, 3)
option = ['rock', 'paper', 'scissor']
computer_move = option[random_number - 1]
print('Enter your move Rock or Paper or Scissor')
human_move = str(input('')).lower()
print(f'Your Move {human_move}, Computer Move {computer_move}')
if human_move == 'rock' or human_move == 'paper' or human_move == 'scissor':
    if human_move == computer_move:
        print('Its Draw')
    elif human_move == 'paper' and computer_move == 'scissor':
        print('Computer Win')
    elif human_move == 'scissor' and computer_move == 'rock' :
        print('Computer Win')
    elif human_move == 'rock' and computer_move == 'paper' :
        print('Computer Win')
    else:
        print('You Win')
else:
    print('False command, Enter your move Rock or Paper or Scissor')
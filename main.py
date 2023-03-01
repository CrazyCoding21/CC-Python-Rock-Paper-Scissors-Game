import random

print('Rock, paper, scissors STARTED! You can choose Rock, Paper or Scissors. You have 3 lives. You need to win 3 times')
comAnswers = ['rock', 'paper', 'scissors']

lives = 3
victories = 0

while True:
    random.shuffle(comAnswers)
    comAnswer = comAnswers[0]

    answer = input('\nYou can choose Rock/Paper/Scissors:\n')
    if answer.isdigit():
        print('It should be a string!')
        continue
    elif answer not in comAnswers:
        print('Invalid variant!')
        continue
    else:
        answer = answer.lower()

    print(answer + ' - ' + comAnswer)

    if answer == 'rock' and comAnswer == 'scissors':
        print('You win!')
        victories += 1
        print('You lives:', lives)
        if victories == 3:
            print('You WIN the game!')
            quit()
    elif answer == 'paper' and comAnswer == 'rock':
        print('You win!')
        victories += 1
        print('You lives:', lives)
        if victories == 3:
            print('You WIN the game!')
            quit()
    elif answer == 'scissors' and comAnswer == 'paper':
        print('You win!')
        victories += 1
        print('You lives:', lives)
        if victories == 3:
            print('You WIN the game!')
            quit()
    elif answer == comAnswer:
        print('Draw!')
        print('You lives:', lives)
    else:
        print('Computer win!')
        lives -= 1
        print('You lives:', lives)
        if lives == 0:
            print('Game Over!')
            quit()
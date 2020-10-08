# Snake Water Gun
print('                                                     WELCOME TO THE\n '
      '                                                 SNAKE WATER GUN GAME\n')
import random
lst=['snake','water','gun']
chance=10
guess_left=1
human=0
computer=0
while(guess_left<=chance):
    inp=input('\n                           enter s for Snake\n                                 w for Water\n                                 g for Gun')
    comp=random.choice(lst)
    if inp=='s' and comp=='snake':
        print(f'try again!\nyour guess=snake and computer guess={comp}      computer point={computer} and human point={human}')
    elif inp=='s' and comp=='water':
        human+=1
        print(f'great\nyour guess=snake and computer guess={comp}       computer point={computer} and human point={human}')
    elif inp=='s' and comp=='gun':
        computer+=1
        print(f'you suck\nyour guess=snake and computer guess={comp}        computer point={computer} and human point={human}')
    elif inp=='w' and comp=='water':
        print(f'try again!\nyour guess=water and computer guess={comp}      computer point={computer} and human point={human}')
    elif inp=='w' and comp=='gun':
        human += 1
        print(f'great\nyour guess=water and computer guess={comp}       computer point={computer} and human point={human}')
    elif inp=='w' and comp=='snake':
        computer += 1
        print(f'you suck\nyour guess=water and computer guess={comp}        computer point={computer} and human point={human}')
    elif inp=='g' and comp=='gun':
        print(f'try again!\nyour guess=gun and computer guess={comp}        computer point={computer} and human point={human}')
    elif inp=='g' and comp=='snake':
        human += 1
        print(f'great\nyour guess=gun and computer guess={comp}     computer point={computer} and human point={human}')
    elif inp=='g' and comp=='water':
        computer += 1
        print(f'you suck\nyour guess=gun and computer guess={comp}      computer point={computer} and human point={human}')
    guess_left+=1
if guess_left>10:
    if computer>human:
        print('                                                     You lose')
        print('                                                    Game Over')
    elif computer<human:
        print('                                                     You won')
        print('                                                    Game Over')
    else:
        print('                                                     it\'s a tie')
        print('                                                    Game Over')
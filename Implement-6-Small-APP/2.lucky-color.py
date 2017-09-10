"""
choice(seq) method of random.Random instance
    Choose a random element from a non-empty sequence.

每猜錯一次顏色，就把猜 錯的從 list拿掉.
"""
import random

colors = ['red', 'blue', 'green', 'purple', 'yellow']
luckyColor = random.choice(colors)

for i in range(3):
    print('There are {} colors'.format(colors))
    guess = input('Guess your lucky color: ')
    if guess != luckyColor:
        print('Seems like {} is not your lucky color:('.format(guess))
        colors.remove(guess)
    else:
        break

if guess == luckyColor:
    print('Great! {} is your lucky color!'.format(luckyColor))
else:
    print('Actually, {} is your lucky color!'.format(luckyColor))







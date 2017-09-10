"""
try and except ，是很我很少用的功能，

但要加入，比較好。
"""
myDict = {
    'apple': ['a round fruit with red skin', '蘋果'],
    'banana': ['a long fruit with yellow skin', '香蕉'],
    'watermelon': ['a large, round fruit with green skin', '西瓜']
    }

def list_all_words():
    print('Your word list\n')
    for key, value in myDict.items():
        print('{} ({})\n{}'.format(key, value[1], value[0]))


def test_yourself():
    quit_the_test = False
    points = 0
    incorrect_word_list = []
    for key, value in myDict.items():
        while True:
            answer = input('\nWhich word matches the definition? or [c]hinese, [p]ass, [q]uit\n{}\n'.format(value[0]))
            if answer == 'c':
                print(value[1])
            elif answer == 'p':
                print('The correct answer is {}'.format(key))
                incorrect_word_list.append(key)
                break
            elif answer == 'q':
                quit_the_test = True
                break
            elif answer == key:
                points += 1
                print('Correct!')
                break
            else:
                print('It\'s not correct')

        if quit_the_test == True:
            break

    print('\nScore {}/{}'.format(points, len(myDict)))
    print('Incorrect words list:')
    for key in incorrect_word_list:
        value = myDict[key]
        print('{} ({})\n{}'.format(key, value[1], value[0]))

def run():
    while True:
        cmd = input("""\nWelcome to your dictionary!
1) Test yourself!
2) List all words
3) Exit\n""")
        if cmd == '1':
            test_yourself()
        elif cmd == '2':
            list_all_words()
        elif cmd == '3':
            break

run()



"""
def new_word():
    try:
        word, definition, chinese = input('Enter your new word (word,definition,chinese):\n').split(',')
        if word in myDict:
            print('{} is already in dictionary'.format(word))
        else:
            myDict[word] = [definition, chinese]
            print('word {} added.'.format(word))
    except ValueError:
        print('Please make sure the format is correct.')
    except:
        print('Something happened unexpected!')

def remove_a_word():
    word = input('Enter a word to remove: ')
    if word in myDict:
        del(myDict[word])
        print('{} has been removed.'.format(word))
    else:
        print('Can not find the word {} in your dictionary'.format(word))

"""


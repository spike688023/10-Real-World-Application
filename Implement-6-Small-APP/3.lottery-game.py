import random

cash = 2000

def create_winning_numbers():
    winning_numbers = set()
    while len(winning_numbers) < 6:
        winning_numbers.add(random.randint(1, 20))
    return winning_numbers

def buy_lottery_ticket():
    global cash
    cash -= 50
    entered_numbers = input('Enter 6 numbers: ')
    entered_numbers_list = entered_numbers.split(',')
    ticket_numbers = {int(n) for n in entered_numbers_list}
    return ticket_numbers

def drawing_result(ticket_numbers, winning_numbers):
    print('Winning numbers are {}'.format(winning_numbers))
    numbers_matched = ticket_numbers.intersection(winning_numbers)
    prizes = [0, 0, 0, 400, 2000, 40000, 100000000]
    prize = prizes[len(numbers_matched)]
    if prize > 0:
        global cash
        cash += prize
        return 'You matched {} numbers, and you just won {} NTD!!'.format(len(numbers_matched), prize)
    else:
        return 'Better luck next time!!'



if __name__ == "__main__":
    while True:
        cmd = input('Welcome to Lottery store.\nDo you [b]uy, [c]heck balance or [l]eave? ')
        if cmd == 'b':
            ticket_numbers = buy_lottery_ticket()
            winning_numbers = create_winning_numbers()
            msg = drawing_result(ticket_numbers, winning_numbers)
            print(msg)
        elif cmd == 'c':
            print(cash)
        elif cmd == 'l':
            break



"""
randint(a, b) method of random.Random instance
    Return random integer in range [a, b], including both end points.

一直都沒特別記， 各種 不同框 ，代表不同資料儲存類型，

list  []  最常見  常用
tuple ()
dict,set {}  差別在於， dict會給 key跟value ， key:value
             如果不是這種型式的，就是set.

>>> dic1 = {1,2,3,4}
>>> dir(dic1)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']

intersection(...) method of builtins.set instance
    Return the intersection of two sets as a new set.

"""

import random
import time

class Witch:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return '{} (lv{})'.format(self.name, self.level)

    def witchcraft_attack(self):
        return random.randint(1, 10) * self.level

class FireWitch(Witch):
    def __init__(self, name, level, fire_staff):
        super().__init__(name, level)
        self.fire_staff = fire_staff

    def witchcraft_attack(self):
        base_attack = super().witchcraft_attack()
        if self.fire_staff:
            print('Witchcraft is filling with fire!!!')
            return base_attack * 2
        else:
            return base_attack

class EvilWitch(Witch):
    def __init__(self, name, level, black_staff_level):
        super().__init__(name, level)
        self.black_staff_level = black_staff_level

    def witchcraft_attack(self):
        base_attack = super().witchcraft_attack()
        print('Witchcraftd with black  staff level {}!!'.format(self.black_staff_level))
        return base_attack * 2 * self.black_staff_level

class Hunter:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def attack(self, witch, critical_strike):
        base_damage = random.randint(1, 10) * self.level
        hunter_damage = base_damage * 2 if critical_strike else base_damage
        witch_damage = witch.witchcraft_attack()

        critical_strike_msg = ' (critical strike!)' if critical_strike else ''
        print('You attacked {}{}'.format(hunter_damage, critical_strike_msg))
        print('Witch attacked {}'.format(witch_damage))

        if hunter_damage > witch_damage:
            print('You defeated {}'.format(witch.name))
            return True
        else:
            print('{} ran away!'.format(witch.name))
            return False


def start_game():
    hunter = Hunter('hunter', 1)

    while True:
        witches = [Witch('witch', random.randint(1, 5)),
                   FireWitch('fire witch', random.randint(6, 20), random.choice([True, False])),
                   EvilWitch('evil witch', random.randint(21, 30), random.randint(1, 3))]
        witch = random.choice(witches)
        print('\n{} has appeared!\n'.format(witch))
        cmd = input('Do you [a]ttack or [s]top tracing? ')
        if cmd == 'a':
            if hunter.attack(witch, random.choice([True, False])):
                hunter.level += 1
                print('Level up! {} level now'.format(hunter.level))
            else:
                print('Hunter is taking time to recover')
                time.sleep(1)
        else:
            print('Hunter stop tracing')

start_game()

"""
遇到女巫， 是計算當下我的功擊力跟女巫的攻擊力，

誰大就誰win， 我還多一個爆集參數， 但50％，

就 True False而已。

功擊計算，是用隨機變數值 成上自身等級。

火巫會不會發 火球  也是50%.  發火球 也只是

攻擊力成二倍。

attack()  會傳入 女巫的物件，以及 是否爆集。

witch 是隨機從三個中， 選一個出來。

這就 一直打女巫，完全不會停。
"""
"""
class 內的self , 有篇文章寫的很好，

这里先理解下函数参数里面的self和cls.这个self和cls是对类或者实例的绑定,对于一般的函数来说我们可以这么调用foo(x),这个函数就是最常用的,它的工作跟任何东西(类,实例)无关.对于实例方法,我们知道在类里每次定义方法的时候都需要绑定这个实例,就是foo(self, x),为什么要这么做呢?因为实例方法的调用离不开实例,我们需要把实例自己传给函数,调用的时候是这样的a.foo(x)(其实是foo(a, x))

Reference:
https://github.com/taizilongxu/interview_python#10-args-and-kwargs


>>> from datetime import datetime
>>> now = datetime.now()
>>> print(str(now))
2017-04-22 15:41:33.012917
>>> print(repr(now))
datetime.datetime(2017, 4, 22, 15, 41, 33, 12917)
通过 str() 的输出结果我们能很好地知道 now 实例的内容，但是却丢失了 now 实例的数据类型信息。而通过 repr() 的输出结果我们不仅能获得 now 实例的内容，还能知道 now 是 datetime.datetime 对象的实例。

因此 str() 与 repr() 的不同在于：

str() 的输出追求可读性，输出格式要便于理解，适合用于输出内容到用户终端。
repr() 的输出追求明确性，除了对象内容，还需要展示出对象的数据类型信息，适合开发和调试阶段使用。

>>> datetime.__repr__
<slot wrapper '__repr__' of 'datetime.datetime' objects>

Reference:
http://www.jianshu.com/p/2a41315ca47e

"""

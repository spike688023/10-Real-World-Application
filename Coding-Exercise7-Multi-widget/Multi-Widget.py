from tkinter import *
from tkinter import ttk

def Convert(*args):
    grams.set( float( value.get() ) * 1000)
    pounds.set( float( value.get() ) * 2.20462)
    ounces.set( float( value.get() ) * 35.274)
    pass

root = Tk()
root.title("KG Convert")

mainframe = ttk.Frame(root, padding="4 4 14 14")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

value = StringVar()
grams = StringVar()
pounds = StringVar()
ounces = StringVar()

ttk.Label(mainframe, text="Kg").grid(column=0, row=1, sticky=E)
ttk.Button(mainframe, text="Convert", command=Convert).grid(column=2, row=1, sticky=(W, E))

words_entry = ttk.Entry(mainframe, width=7, textvariable=value)
words_entry.grid(column=1, row=1, sticky=(W, E))

ttk.Entry(mainframe, width=7, textvariable=grams).grid(column=0, row=2, sticky=(W, E))

ttk.Entry(mainframe, width=7, textvariable=pounds).grid(column=1, row=2, sticky=(W, E))

ttk.Entry(mainframe, width=7, textvariable=ounces).grid(column=2, row=2, sticky=(W, E))

# ???
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

words_entry.focus()
root.bind('<Return>', Convert)

#This final line tells Tk to enter its event loop, which is needed to make everything run.
root.mainloop()

"""

大多的用法，建立在ttk這個物件， ttk.Label().grid()

同時建立起物件，還給 定了坐標， 前面還可以放個變數去接，

更大型的寫法，可能tkk物 件之間會有互動，而我這題 很簡單，

所以不用。

這句代表，一開始輸入的遊標，是放在這個上。
words_entry.focus()

這句是指， 呼叫Convert 這個function button 時，可以用enter回傳，

不一定要按button.
root.bind('<Return>', Convert)

這裡使用enter時，發 生一個錯誤 如下：
問題 出在Convert(*args) 如果裡面沒加*args，會出現以下錯誤，

加了就 沒事了。
這裡是猜  把 <Return> 當參數放入function Convert ，

所以才會出現以下錯誤 。
TypeError: Convert() takes 0 positional arguments but 1 was given

Reference:
http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html
http://www.tkdocs.com/tutorial/firstexample.html
"""

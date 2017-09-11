from tkinter import *
from tkinter import ttk

file = open("98_spike.txt","w+")

def add():
    file.write(words.get()+"\n")
    words_entry.delete(0,100)
    words_entry.focus()

def save():
    file.write(words.get()+"\n")
    file.flush()
    words_entry.delete(0,100)
    words_entry.focus()

def SaveAndClose():
    file.write(words.get()+"\n")
    file.close()
    root.destroy()

root = Tk()
root.title("Lines Recorder")

mainframe = ttk.Frame(root, padding="4 4 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

words = StringVar()

words_entry = ttk.Entry(mainframe, width=7, textvariable=words)
words_entry.grid(column=0, row=0, sticky=(W, E))

ttk.Button(mainframe, text="Add Line", command=add).grid(column=1, row=0, sticky=(W, E))
ttk.Button(mainframe, text="Save changes", command=save).grid(column=2, row=0, sticky=(W, E))
ttk.Button(mainframe, text="Save and Close", command=SaveAndClose).grid(column=3, row=0, sticky=(W, E))


for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

words_entry.focus()
#root.bind('<Return>', calculate)

root.mainloop()

"""

Reference:
http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html
http://www.tkdocs.com/tutorial/firstexample.html
"""

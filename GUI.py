# ---------------------------------------import---------------------------------------------------
from Trie import *
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox


# ---------------------------------------trie---------------------------------------------------
myTrie = Trie()
# ---------------------------------------open file---------------------------------------------------
global file
def open_file():
    file_open = filedialog.askopenfilename(title='Open a text file | MJ')
    file = open(file_open) # Open file
    myTrie.formTrie(file)
    myTrie.printAutoSuggestionsGUI(combo.get() , combo)
    file.close()

# ---------------------------------------creat---------------------------------------------------
def creator():
        tkinter.messagebox.showinfo("Creator | MJ", "This Search Engine has been created by MJ :|")

# ---------------------------------------help---------------------------------------------------
def help():
        tkinter.messagebox.showinfo("Help | MJ", "first open your file and enter your Key and then open the drop-down list.")

# ---------------------------------------choose Number method---------------------------------------------------
def chooseNumber(event):
    comp = myTrie.printAutoSuggestionsGUI(combo.get() , combo)

# ---------------------------------------window---------------------------------------------------
def gui():
    window=Tk() # Object of Tk
    
    window.title("Search Engine | MJ") # window Title
    window.geometry('300x200') # Size of window
    window.resizable(width=False, height=False)
    color = "#E6E6E6"
    window.configure(bg=color)
    # ----------------------------frame----------------------------
    top_1 = Frame(window, width=400, height=20, bg=color)
    top_1.pack(side="top")
    top_2 = Frame(window, width=400, height=20, bg=color)
    top_2.pack(side="top")
    top_3 = Frame(window, width=400, height=20, bg=color)
    top_3.pack(side="top")
    top_4 = Frame(window, width=400, height=20, bg=color)
    top_4.pack(side="top")
    top_5 = Frame(window, width=400, height=20, bg=color)
    top_5.pack(side="top")
    top_6 = Frame(window, width=400, height=20, bg=color)
    top_6.pack(side="top")
    top_7 = Frame(window, width=400, height=20, bg=color)
    top_7.pack(side="top")
    top_8 = Frame(window, width=400, height=20, bg=color)
    top_8.pack(side="top")

# ---------------------------------------lable---------------------------------------------------
    label_1 = Label(top_1, text = "Please Enter Your Key :", bg=color)
    label_1.pack()

    global var
    var = tk.StringVar()


    global combo
    combo = ttk.Combobox(top_2 , width= 25 , textvariable=var)
    combo.pack()
    combo.bind("<KeyRelease>" ,chooseNumber)

# ---------------------------------------button---------------------------------------------------
    btn_choose = Button(top_8,text="Open File", command=lambda: open_file())
    btn_choose.pack(side=LEFT, padx=5,pady=5)

    btn_creat = Button(top_8, text="creator", command=lambda: creator())
    btn_creat.pack(side=LEFT, padx=5,pady=5)

    btn_help = Button(top_8, text="help", command=lambda: help())
    btn_help.pack(side=LEFT, padx=5,pady=5)

    mainloop()
gui()
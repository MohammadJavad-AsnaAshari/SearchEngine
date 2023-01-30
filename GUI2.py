# ---------------------------------------import---------------------------------------------------
import tkinter as tk
import re  # import regular expression library
from tkinter import END
from Trie import *
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tkinter.messagebox
import tkinter as tk

# ---------------------------------------trie---------------------------------------------------
myTrie = Trie()
# ---------------------------------------open file---------------------------------------------------
global file


# def open_file():
#     file_open = filedialog.askopenfilename(title='Open a text file | MJ')
#     file = open(file_open)  # Open file
#     myTrie.formTrie(file)
#     myTrie.printAutoSuggestionsGUI(combo.get(), combo)
#     file.close()


my_list = ['aecde', 'adba', 'acbd', 'abcd', 'abded',
           'bdbd', 'baba', 'bcbc', 'bdbd']  # data source list,

# ---------------------------------------function---------------------------------------------------
# ---------------------------------------creat---------------------------------------------------
def creator():
    tkinter.messagebox.showinfo(
        "Creator | MJ", "This Search Engine has been created by MJ :|")

# ---------------------------------------help---------------------------------------------------
def help():
    tkinter.messagebox.showinfo(
        "Help | MJ", "first open your file and enter your Key and then open the drop-down list.")

# ---------------------------------------choose Number method---------------------------------------------------
# def chooseNumber(event):
#     comp = myTrie.printAutoSuggestionsGUI(combo.get(), combo)



# ---------------------------------------window---------------------------------------------------
my_window = tk.Tk()

my_window.geometry("300x200")  # Size of the window
my_window.title("Search Engine | MJ")  # Adding a title
font1 = ('Times', 12, 'bold')  # font size and style
my_window.resizable(width=False, height=False)
color = "#E6E6E6"
my_window.configure(bg=color)


# global combo
# combo = ttk.Combobox(top_2, width=25, textvariable=var)
# combo.pack()
# combo.bind("<KeyRelease>", chooseNumber)

# lbl_1 = tk.Label(text='Autocomplete', font=font1)  # adding label at top
# lbl_1.grid(row=0, column=1)

# ----------------------------frame----------------------------
top_1 = Frame(my_window, width=400, height=20, bg=color)
top_1.pack(side="top")
top_2 = Frame(my_window, width=400, height=20, bg=color)
top_2.pack(side="top")
top_3 = Frame(my_window, width=400, height=20, bg=color)
top_3.pack(side="top")
top_4 = Frame(my_window, width=400, height=20, bg=color)
top_4.pack(side="top")
top_5 = Frame(my_window, width=400, height=20, bg=color)
top_5.pack(side="top")
top_6 = Frame(my_window, width=400, height=20, bg=color)
top_6.pack(side="top")
top_7 = Frame(my_window, width=400, height=20, bg=color)
top_7.pack(side="top")
top_8 = Frame(my_window, width=400, height=20, bg=color)
top_8.pack(side="top")
top_9 = Frame(my_window, width=400, height=20, bg=color)
top_9.pack(side="top")
top_10 = Frame(my_window, width=400, height=20, bg=color)
top_10.pack(side="top")

# ---------------------------------------lable---------------------------------------------------
label_1 = Label(top_1, text="Please Enter Your Key :", bg=color, font=font1)
label_1.pack()

# ---------------------------------------button---------------------------------------------------
btn_creat = Button(top_4, text="creator", command=lambda: creator())
btn_creat.pack(side=LEFT, padx=5,pady=5)

btn_help = Button(top_4, text="help", command=lambda: help())
btn_help.pack(side=LEFT, padx=5,pady=5)

# ---------------------------------------functions---------------------------------------------------


def my_upd(my_widget):  # On selection of option
    my_window = my_widget.widget
    index = int(my_window.curselection()[0])  # position of selection
    value = my_window.get(index)  # selected value
    e1_str.set(value)  # set value for string variable of Entry
    list_box_1.delete(0, END)     # Delete all elements of Listbox


def my_down(my_widget):  # down arrow is clicked
    list_box_1.focus()  # move focus to Listbox
    list_box_1.selection_set(0)  # select the first option


e1_str = tk.StringVar()  # string variable
e1 = tk.Entry(top_2, textvariable=e1_str, font=font1)  # entry
e1.pack()


global var
var = tk.StringVar()

# listbox
global list_box_1
list_box_1 = tk.Listbox(top_3,  height=5, font=font1,
                        relief='flat', bg=color)
list_box_1.pack()
# list_box_1.bind("<KeyRelease>", chooseNumber)


def get_data(*args): # populate the Listbox with matching options
    search_str=e1.get() # user entered string
    list_box_1.delete(0,END)     # Delete all elements of Listbox
    for element in my_list:
        if(re.match(search_str,element,re.IGNORECASE)):
            list_box_1.insert(tk.END,element)#add matching options to Listbox
#l1.bind('<<ListboxSelect>>', my_upd)
e1.bind('<Down>', my_down) # down arrow key is pressed
list_box_1.bind('<Right>', my_upd) # right arrow key is pressed
list_box_1.bind('<Return>', my_upd)# return key is pressed
e1_str.trace('w',get_data) #
#print(my_w['bg']) # reading background colour of window


my_window.mainloop()  # Keep the window open

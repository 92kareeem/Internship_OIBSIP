import random
import string
from tkinter import *
import pyperclip

root = Tk()
root.geometry("600x600")
root.title("Random Password Generator") 
output_pass = StringVar()

comb_all = [
    string.punctuation,
    string.ascii_uppercase,
    string.digits,
    string.ascii_lowercase,
]
def randompass():
    password = ""  
    for y in range(Pass_Length.get()):
        char_type = random.choice(comb_all) 
        password = password + random.choice(char_type)
    output_pass.set(password)
def Pass_cpy():
    pyperclip.copy(output_pass.get())
Pass_head = Label(root, text='Password Length', font='Helvetica 16 bold', bg='cyan')
Pass_head.pack(pady=10)  

Pass_Length = IntVar() 
length = Spinbox(root, from_=4, to=128, textvariable=Pass_Length, width=24, font='Helvetica 16')
length.pack()

generate_button = Button(
    root,
    command=randompass,
    text="Generate Password",
    font="Arial 12",
    bg='lightgreen',
    fg='black',
    activebackground="green",
    padx=10,
    pady=10,
)
generate_button.pack(pady=20)

Pass_Lbl = Label(root, text='Random Generated Password', font='Helvetica 16 bold', bg='yellow')
Pass_Lbl.pack(pady="30 10")

Entry(root, textvariable=output_pass, width=24, font='Helvetica 16').pack()

button_cpy = Button(
    root,
    text='Copy to Clipboard',
    command=Pass_cpy,
    font="Arial 12",
    bg='lightblue',
    fg='black',
    activebackground="teal",
    padx=10,
    pady=10,
)
button_cpy.pack(pady=20)

root.mainloop()

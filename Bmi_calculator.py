from tkinter import *
from tkinter import messagebox

def reset():
    age_yrs.delete(0, 'end')
    height_feet.delete(0, 'end')
    height_inches.delete(0,'end')
    weight_mgs.delete(0, 'end')

def calculate_bmi():
    mgs = int(weight_mgs.get())
    feet = int(height_feet.get())
    inches = int(height_inches.get())
    height_in_cm = (feet * 12 + inches) * 2.54  # Convert feet and inches to cm
    m = height_in_cm / 100  # Convert height to meters
    bmi = mgs / (m * m)
    bmi = round(bmi, 1)
    bmi_index(bmi)

def bmi_index(bmi):
    if bmi < 18.5:
        messagebox.showinfo('BmI Calculator', f'BmI = {bmi} is Underweight')
    elif 18.5 <= bmi < 24.9:
        messagebox.showinfo('BmI Calculator', f'BmI = {bmi} is Normal')
    elif 24.9 <= bmi < 29.9:
        messagebox.showinfo('BmI Calculator', f'BmI = {bmi} is Overweight')
    elif bmi >= 29.9:
        messagebox.showinfo('BmI Calculator', f'BmI = {bmi} is Obesity')
    else:
        messagebox.showerror('BmI Calculator', 'Something went wrong!')

ws = Tk()
ws.title('BmI Calculator')
ws.geometry('600x500')
ws.config(bg='#add8e6')

frame = Frame(
    ws,
    padx=10,
    pady=10,
    bg='#d3d3d3'
)
frame.pack(expand=True)

age_lb = Label(
    frame,
    text="Enter Age of the person",
    bg='#f0f0f0'
)
age_lb.grid(row=1, column=0)

age_yrs = Entry(
    frame,
)
age_yrs.grid(row=1, column=1, pady=5)

ht = Label(
    frame,
    text='Select Gender of the person',
    bg='#f0f0f0'
)
ht.grid(row=2, column=0)

var = IntVar()

male_button = Radiobutton(
    frame,
    text='male',
    variable=var,
    value=1,
    bg='#f0f0f0'
)
male_button.grid(row=2,column=1)

female_button = Radiobutton(
    frame,
    text='Female',
    variable=var,
    value=2,
    bg='#f0f0f0'
)
female_button.grid(row=2, column=2)

ht = Label(
    frame,
    text="Enter Height(ft & inches) of the person",
    bg='#f0f0f0'
)
ht.grid(row=3,column=0)

height_feet = Entry(
    frame,
    width=7
)
height_feet.grid(row=3,column=1,padx=(5,0),pady=5)

height_feet_label = Label(
    frame,
    text="feet",
    bg='#f0f0f0'
)
height_feet_label.grid(row=3,column=2,padx=(0,5))

height_inches = Entry(
    frame,
    width=5
)
height_inches.grid(row=3, column=3, padx=(5,0), pady=5)

height_inches_label = Label(
    frame,
    text="inches",
    bg='#f0f0f0'
)
height_inches_label.grid(row=3, column=4,padx=(0,7))

weight_lb = Label(
    frame,
    text="Enter Weight(mgs) of the person",
    bg='#f0f0f0'
)
weight_lb.grid(row=4, column=0)

height_tf = Entry(
    frame,
)
height_tf.grid(row=4, column=1, pady=5)

weight_mgs = Entry(
    frame,
)
weight_mgs.grid(row=4, column=1, pady=5)

frame3 = Frame(
    frame,
    bg='#f0f0f0'
)
frame3.grid(row=5, columnspan=5, pady=10)

cal_btn = Button(
    frame3,
    text='Calculate',
    command=calculate_bmi,
    bg='#4caf50',
    fg='white'
)
cal_btn.pack(side=LEFT, padx=5)

reset_btn = Button(
    frame3,
    text='Reset',
    command=reset,
    bg='#f44336',
    fg='white'
)
reset_btn.pack(side=LEFT, padx=5)

exit_btn = Button(
    frame3,
    text='Exit',
    command=lambda: ws.destroy(),
    bg='#2196f3',
    fg='white'
)
exit_btn.pack(side=RIGHT, padx=5)

ws.mainloop()

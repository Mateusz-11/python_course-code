import tkinter as tk
from tkinter import messagebox
from random import randint

def on_submit():
    global previous_difference, steps
    steps += 1
    value = int(field.get())
    difference = abs(target - value)

    if difference == 0:
        messagebox.showinfo('Condition', f"Congratulation! You guessed in {steps} steps.")
    elif previous_difference is None or difference < previous_difference:
        messagebox.showinfo('Condition', "Getting warmer")
    else:
        messagebox.showinfo('Condition', "Getting colder")

    previous_difference = difference

steps = 0
previous_difference = None
target = randint(1,100)

window = tk.Tk()
window.title('Guess number')

label = tk.Label(window, text='Write number')
label.pack()

field = tk.Entry()
field.pack()

button = tk.Button(text="Guess!", command=on_submit)
button.pack()

window.mainloop()
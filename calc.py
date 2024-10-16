# калькулятор

import tkinter as tk
from multiprocessing.connection import answer_challenge

def get_values():
    return int(number1_entry.get()), int(number2_entry.get())

def insert_value(value):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, value)

def add():
    n1, n2 = get_values()
    insert_value(n1 + n2)

def sub():
    n1, n2 = get_values()
    insert_value(n1 - n2)

def div():
    n1, n2 = get_values()
    insert_value(n1 / n2)

def mul():
    n1, n2 = get_values()
    insert_value(n1 * n2)

window = tk.Tk()
window.title("калькулятор")
window.geometry("350x350")
window.resizable(False, False)

button_add = tk.Button(window, width=2, height=2, text='+', command=add)
button_add.place(x=100, y=200)
button_sub = tk.Button(window, width=2, height=2, text='-', command=sub)
button_sub.place(x=150, y=200)
button_mul = tk.Button(window, width=2, height=2, text='*', command=mul)
button_mul.place(x=200, y=200)
button_div = tk.Button(window, width=2, height=2, text='/', command=div)
button_div.place(x=250, y=200)

number1_entry = tk.Entry(window, width=28)
number1_entry.place(x=100, y=75)
number2_entry = tk.Entry(window, width=28)
number2_entry.place(x=100, y=150)
answer_entry = tk.Entry(window, width=28)
answer_entry.place(x=100, y=300)

label1 = tk.Label(window, text="Задайете первое число")
label1.place(x=100, y=50)
label2 = tk.Label(window, text="Задайете второе число")
label2.place(x=100, y=125)
label3 = tk.Label(window, text="Ответ")
label3.place(x=100, y=275)

window.mainloop()

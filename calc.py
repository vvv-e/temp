# калькулятор

import tkinter as tk
from multiprocessing.connection import answer_challenge

window = tk.Tk()
window.title("калькулятор")
window.geometry("350x350")
window.resizable(False,False)

button_add = tk.Button(window, width=2, height=2, text='+' )
button_add.place(x=100, y=200)
button_sub = tk.Button(window, width=2, height=2, text='-' )
button_sub.place(x=150, y=200)
button_mul = tk.Button(window, width=2, height=2, text='*' )
button_mul.place(x=200, y=200)
button_div = tk.Button(window, width=2, height=2, text='/' )
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


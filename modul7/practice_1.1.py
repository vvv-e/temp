import os
import tkinter
from tkinter import filedialog
from tkinter import messagebox as mb

if __name__ == "__main__":
    def file_select():
        filename = filedialog.askopenfilename(initialdir=".", title="Выберите файл",
                                              filetypes=(("Текстовый файл", ".txt"), ("Все файлы", "*")))
        text['text'] = 'Файл: ' + filename
        os.startfile(filename)


    def menu_file_info():
        mb.showinfo(message="Пользоваться нашим блокнотом просто", title="Info")


    def menu_file_about():
        mb.showinfo(message="Аффтор: Вв.В", title="About")


    window = tkinter.Tk()
    window.title('Проводник')
    window.geometry('450x150')
    window.configure(bg='black')
    window.resizable(False, False)
    text = tkinter.Label(window, text='Файл:', height=5, width=65, background='silver')
    text.grid(column=1, row=1)
    button_select = tkinter.Button(window, width=20, height=3, text='Выбрать файл', command=file_select)
    button_select.grid(column=1, row=2)

    menubar = tkinter.Menu()
    menubar.add_command(label="Info", underline=0, command=menu_file_info)
    menubar.add_command(label="About", underline=0, command=menu_file_about)
    window.config(menu=menubar)

    window.mainloop()

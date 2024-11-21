import tkinter
from tkinter import messagebox as mb

class App(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        menubar = tkinter.Menu(self)
        menubar.add_command(label="Info", underline=0, command=self.menu_file_info)
        menubar.add_command(label="About", underline=0, command=self.menu_file_about)
        self.config(menu=menubar)

    def menu_file_info(self):
        mb.showinfo(message="Пользоваться нашим блокнотом просто", title="Info" )

    def menu_file_about(self):
        mb.showinfo(message="Аффтор: Вв.В", title="About")

if __name__ == "__main__":
    app = App()
    app.mainloop()


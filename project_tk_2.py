from tkinter import Tk, Frame, Menu


class Window():
    def __init__(self):
        self.__window = Tk()
        self.__set_window()
        self.__set_menu()


    def __set_window(self):
        self.__window.geometry("700x500")
        self.__window.minsize(500, 200)
        self.__window.title("Some Text")
        self.__window.iconbitmap("icon.ico")

    def start_window(self):
        self.__window.mainloop()

    def __set_menu(self):
        self.__menubar = Menu(self.__window)
        self.__file= Menu(self.__menubar, tearoff=0)


        self.__file.add_command(label = "Exit", underline=1, accelerator="Ctrl + C")
        self.__menubar.add_cascade(label="File", underline=0, )

        self.__menubar.add_cascade(label="Edit", underline=1)


        self.__menubar.add_cascade(label="Help", underline=0)
        self.__window["menu"] = self.__menubar

    def run(self):
        self.__window.mainloop()

a=Window()

a.run()
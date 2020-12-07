#!/usr/bin/python3
# -*- coding:utf-8 -*-

from tkinter import *
from tkinter.ttk import *


class Application_ui(Frame):
    # 这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('使用vb6插件生成界面')
        self.master.geometry('312x206')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        #  self.style = Style()

        self.Command2Var = StringVar(value='退出')
        self.Command2 = Button(self.top, text='退出', textvariable=self.Command2Var, command=self.Command2_Cmd)
        self.Command2.setText = lambda x: self.Command2Var.set(x)
        self.Command2.text = lambda: self.Command2Var.get()
        self.Command2.place(relx=0.538, rely=0.66, relwidth=0.337, relheight=0.238)

        self.Command1Var = StringVar(value='测试')
        self.Command1 = Button(self.top, text='测试', textvariable=self.Command1Var, command=self.Command1_Cmd)
        self.Command1.setText = lambda x: self.Command1Var.set(x)
        self.Command1.text = lambda: self.Command1Var.get()
        self.Command1.place(relx=0.128, rely=0.66, relwidth=0.337, relheight=0.238)

        self.Text1Var = StringVar(value='Text1')
        self.Text1 = Entry(self.top, textvariable=self.Text1Var)
        self.Text1.setText = lambda x: self.Text1Var.set(x)
        self.Text1.text = lambda: self.Text1Var.get()
        self.Text1.place(relx=0.256, rely=0.272, relwidth=0.439, relheight=0.238)

        self.Label1Var = StringVar(value='Label1')
        # self.style.configure('TLabel1.TLabel', anchor='w'), style='TLabel1.TLabel'
        self.Label1 = Label(self.top, text='Label1', textvariable=self.Label1Var)
        self.Label1.setText = lambda x: self.Label1Var.set(x)
        self.Label1.text = lambda: self.Label1Var.get()
        self.Label1.place(relx=0.231, rely=0.078, relwidth=0.49, relheight=0.16)


class Application(Application_ui):
    # 这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)

    def Command2_Cmd(self, event=None):
        # sys.exit()
        self.quit()

    def Command1_Cmd(self, event=None):
        self.Label1Var.set(self.Text1Var.get())


if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()
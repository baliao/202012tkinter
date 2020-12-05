#coding:utf-8

import tkinter
from tkinter.ttk import Notebook

win = tkinter.Tk()
win.title('Notebook test')
win.geometry('500x300')

#please take attention order
nb = Notebook(win)
frme1 = tkinter.LabelFrame()
frme2 = tkinter.LabelFrame()
# frme1 = tkinter.Frame()
# frme2 = tkinter.Frame()


lb1 = tkinter.Label(frme1,text='个人信息显示区',bg='red')
lb1.pack(padx=10,pady=10)

lb2 = tkinter.Label(frme2,text='公司业务显示区',bg='green')
lb2.pack()

nb.add(frme1,text='个人信息')
nb.add(frme2,text='公司业务')
nb.pack(padx=5,pady=5,fill=tkinter.BOTH,expand=True)

win.mainloop()
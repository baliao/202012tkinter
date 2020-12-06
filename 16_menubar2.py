#coding:utf-8
import tkinter
from tkinter import messagebox

win= tkinter.Tk()
win.title('menu测试')
win.geometry('600x200')


menubar = tkinter.Menu(win)
filemenu = tkinter.Menu(menubar,tearoff=False,)
menubar.add_cascade(label='File',menu=filemenu,underline=1,)
filemenu.add_command(label='新建',underline=0)
filemenu.add_command(label='退出',underline=0)


helpmenu = tkinter.Menu(menubar,tearoff=False)
menubar.add_cascade(label='帮助(Help)',menu=helpmenu,underline=0)
helpmenu.add_command(label='帮助信息')
helpmenu.add_separator()
helpmenu.add_command(label='升级系统')


win.config(menu=menubar)



win.mainloop()
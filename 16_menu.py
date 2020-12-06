#coding:utf-8
import tkinter
from tkinter import messagebox

win = tkinter.Tk()
win.title('菜单')
win.geometry('500x300')

wholemenubar = tkinter.Menu(win)

filemenu = tkinter.Menu(wholemenubar,tearoff=False)

wholemenubar.add_cascade(label='File',menu=filemenu)

def showfile():
    messagebox.showinfo('新建文件','选择文件')

filemenu.add_command(label='文件',command=showfile)
filemenu.add_command(label='编辑')
filemenu.add_separator()
filemenu.add_command(label='退出',command=win.destroy)
win.config(menu=wholemenubar)

win.mainloop()
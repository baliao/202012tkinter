#coding:utf-8
import tkinter
from tkinter.colorchooser import askcolor
import time

win = tkinter.Tk()
win.title('scale test')
win.geometry('500x350')

#source 必须要的
def show(source):
    lb.config(text='显示的值为:{}'.format(scale1.get()))
    lb.config(bg='red')
    mycolor = askcolor()


scale1 = tkinter.Scale(win,from_=0,to=100,length = 100,orient=tkinter.HORIZONTAL,command=show)
scale1.pack()

def adjust():
    print (scale1.get())
    scale1.set(73)

btn = tkinter.Button(win,text='Move',command=adjust,bg='yellow')
btn.pack()

lb = tkinter.Label(win,text='',)
lb.pack()


win.mainloop()
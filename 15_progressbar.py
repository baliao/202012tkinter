#coding:utf-8
import tkinter,time
from tkinter.ttk import *


win = tkinter.Tk()
win.title('progress bar')
win.geometry('500x200')


# def show(event):
#     for i in range(101):
#         v.set(i)
#         win.update()
#         time.sleep(0.2)

def show(event):
    pb.start()

#mode determinate or indeterminate 从左到右,左右来回...
v = tkinter.IntVar()
pb = Progressbar(win,length=100,mode='indeterminate',orient=tkinter.HORIZONTAL,variable=v)
pb.pack()

pb['maximum'] = 100
pb['value'] = 0

btn = tkinter.Button(win,text='运行',width=100,bg='red')
btn.pack()
btn.bind('<Button-1>',show)





win.mainloop()
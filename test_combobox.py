#coding:utf-8
import tkinter
from tkinter.ttk import Combobox

win= tkinter.Tk()
win.title('combobox test...')
win.geometry('300x500')

var = tkinter.StringVar()
value = ['python','java','c++','R']

#textvariable 方便设置值,value 初始值.

cb = Combobox(win,textvariable=var,value=value)

#虚拟绑定事件<<ComboboxSelected>>

def showmsg(event):
    label.config(text=var.get())

# set or current to default value
cb.set(value[1])
cb.current(3)
cb.pack()
cb.bind('<<ComboboxSelected>>',showmsg)




def show(event):
    print (cb.get())

btn = tkinter.Button(win,text='读取信息',width=100,bg='green')
btn.pack()
btn.bind('<Button-1>',show)


label = tkinter.Label(win,text='显示区域',bg='yellow',width=100)
label.pack()
win.mainloop()
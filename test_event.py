#coding:utf-8
import tkinter

win= tkinter.Tk()
win.title('Event 事件')

win.geometry('300x200')

label1 = tkinter.Label(win,text='确认',bg='green')
label1.pack()

def buttonClicked(event):
    label1.config(text='产生了事件,{},{}'.format(event.x,event.y))
label1.bind('<Button-1>',buttonClicked)

def enter(event):
    text.set('Enter....Hi')
def leave(event):
    text.set('Leave for....,bye')

text = tkinter.StringVar()
label2 = tkinter.Label(win,text='显示器',width=100,bg='red',textvariable=text) #变量
label2.pack()
label2.bind('<Enter>',enter) #鼠标进入
label2.bind('<Leave>',leave) #鼠标离开

win.mainloop()
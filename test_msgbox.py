#coding:utf-8
import tkinter
from tkinter import messagebox


win= tkinter.Tk()
win.title('message box')
win.geometry('300x200')
result = tkinter.messagebox.askquestion(title ='对话框', message = 'are you ok',)
print (result)
v=tkinter.StringVar()
lable = tkinter.Label(win,textvariable=v,width=50,bg='green')
lable.pack()
if result == 'yes':
    v.set('yes click')
else:
    v.set('no clikc')

win.mainloop()
#coding:utf-8
import tkinter
win = tkinter.Tk()
win.title('Frame test')
win.geometry('300x200')


fm_win = tkinter.Frame(win,)
fm1 = tkinter.Frame(fm_win)


lb = tkinter.Label(fm1,text='LABEL',bg='green',width=10,height=2)
lb.pack()

fm_win.pack()
fm1.pack()

win.mainloop()
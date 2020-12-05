import tkinter
import tkinter.ttk as ttk

win = tkinter.Tk()
win.title('test show on the same time')
win.geometry('200x100')

def callback(*args):
    msg = estring.get()
    lstring.set(msg)
    print ('数据输入为:{}'.format(msg))

estring = tkinter.StringVar()
en1 = tkinter.Entry(win,textvariable=estring,)
en1.pack()
estring.trace('w',callback)

lstring = tkinter.StringVar()
label = tkinter.Label(win,textvariable=lstring)
lstring.set('同步显示')
label.pack()






win.mainloop()
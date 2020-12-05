#coding:utf-8
import tkinter

win = tkinter.Tk()
win.title('复选框')
win.geometry('300x200')
banner = tkinter.Label(win,text='请选择你喜欢的运动',bg='red')
banner.pack()

sports = ['篮球','足球','排球','皮球']
#set 0 is uncheck, -1 and 1 are check. then get it value by command
v1 = tkinter.IntVar()
v1.set(0)
chk1 = tkinter.Checkbutton(win,variable=v1,text=sports[0],)
chk1.pack()

v2 = tkinter.IntVar()
v2.set(0)
chk2 = tkinter.Checkbutton(win,variable=v2,text=sports[1],)
chk2.pack()


v3 = tkinter.IntVar()
v3.set(0)
chk3 = tkinter.Checkbutton(win,variable=v3,text=sports[2],)
chk3.pack()

v4 = tkinter.IntVar()
v4.set(0)
chk4 = tkinter.Checkbutton(win,variable=v4,text=sports[3],)
chk4.pack()

def show():
    result = []
    for index,i in enumerate([v1,v2,v3,v4]):
        v = i.get()
        if v:
            result.append(sports[index])
            show_bar.config(text = str(','.join(result)))


confirm = tkinter.Button(win,text='确认',command=show,bg='yellow',width=100)
confirm.pack()

show_bar = tkinter.Label(win,text='',bg='green',width=100)
show_bar.pack()

win.mainloop()
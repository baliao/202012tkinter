import tkinter

win= tkinter.Tk()
win.title('双事件....')
win.geometry('500x200')


def btneven1(event):
    print ('btnevent1...中国事件一')

def btneven2(event):
    print ('btnevent2...中国事件二')

def btneven3(event):
    print ('btnevent3...中国事件三')
#add = '+' 绑定多个事件


btn = tkinter.Button(win,text='确认',bg='red',width=50)
btn.bind('<Button-1>',btneven1,)
# btn.bind('<Button-1>',btneven2,add='+')
btn.bind('<Button-1>',btneven2,add = '+')
btn.bind('<Button-1>',btneven3,add = '+')
btn.pack()

win.mainloop()
import tkinter
win= tkinter.Tk()
win.title('optionMenu test...')
win.geometry('500x400')
var = tkinter.StringVar()
course = ['python','java','c#']
var.set(course[0])
optionMenu1 = tkinter.OptionMenu(win,var,*course)

optionMenu1.pack()


def show(event):
    print (var.get())

btn = tkinter.Button(win,text='读取用户信息',width=100,bg='red',)
btn.pack()
btn.bind('<Button-1>',show)

win.mainloop()
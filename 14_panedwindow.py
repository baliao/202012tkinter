import tkinter

win =tkinter.Tk()
win.title('panedwindow test')
win.geometry('300x500')

pw = tkinter.PanedWindow(orient=tkinter.VERTICAL)
pw.pack(fill=tkinter.BOTH,expand=True)
top = tkinter.Label(pw,text='top')
pw.add(top)
mid = tkinter.Label(pw,text='mid')
pw.add(mid)
botton = tkinter.Label(pw,text='bottom')
pw.add(botton)

pw.mainloop()
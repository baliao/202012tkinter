import tkinter
win=tkinter.Tk()
win.title('Listbox 测试中....')
win.geometry('500x500')


sb1 = tkinter.Scrollbar(win,)
sb1.pack(side = tkinter.RIGHT,fill=tkinter.Y)

#EXTENDEN 表示支持ctrl 选择
v= tkinter.StringVar()
listb1 = tkinter.Listbox(win,background='yellow',listvariable=v,width=100,height=10,selectmode=tkinter.EXTENDED,
                         yscrollcommand=sb1.set)
listb1.pack(side=tkinter.LEFT,fill=tkinter.BOTH,expand=True)

sb1.config(command=listb1.yview)



def readlistbox(event):
    #获取所有条目
    print (v.get())

    #获取当前选择的条目
    userlist = listb1.curselection()
    for index in userlist:
        print ("当前用户选择:{}".format(listb1.get(index)))


btn = tkinter.Button(win,text='读取Listbox',background='red',width=100)
btn.pack()
btn.bind('<Button-1>',readlistbox)

for city in ['BJ','SH','CS','SZ','GZ']:
    # v.set(city)
    #插入条目,从上下往下
    listb1.insert(tkinter.END,city)
    listb1.insert(tkinter.ACTIVE,city)
    listb1.insert(tkinter.END,city)
    listb1.insert(tkinter.ACTIVE,city)
    listb1.insert(tkinter.END,city)
    listb1.insert(tkinter.ACTIVE,city)

win.iconbitmap('icon.ico')
listb1.selection_set(2,3)
win.mainloop()

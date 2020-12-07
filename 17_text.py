#coding:utf-8
import tkinter,time


win= tkinter.Tk()
win.title('text测试中')
win.geometry('400x200')

uscrolbar= tkinter.Scrollbar(win)
text1 = tkinter.Text(win,width=100,height=10)


text1.insert(tkinter.END,'Hello Text')
uscrolbar.pack(side=tkinter.RIGHT,fill=tkinter.Y)
text1.pack()

uscrolbar.config(command=text1.yview)
text1.config(yscrollcommand=uscrolbar.set)
def readmore(event):
    for i in range(100):
        text1.insert(tkinter.END,','.join(str(i),))
        time.sleep(0.01)
        win.update()





btn = tkinter.Button(text='读取信息',bg='red')
btn.pack(side=tkinter.BOTTOM)
btn.bind('<Button-1>',readmore)




win.mainloop()

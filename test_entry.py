#coding:utf-8
import tkinter
import tkinter.ttk as ttk
import datetime,time


win = tkinter.Tk()
win.title('entry test')
win.geometry('500x100')
win.iconbitmap('icon.ico')

label1 = tkinter.Label(win,text='姓名',relief='groove')
label1.grid(row=0)

label2 = tkinter.Label(win,text='年龄',relief='groove')
label2.grid(row=1)

entry1 = tkinter.Entry(win,width=100)
entry1.grid(row=0,column=1,columnspan=8)

entry2 = tkinter.Entry(win,width=100)
entry2.grid(row=1,column=1,columnspan=8)

#使用get 方法获取值
#使用insert 方法写入值
def print_msg():
    user = entry1.get()
    age = entry2.get()
    print ('{},{}'.format(user,age))
    msg = datetime.datetime.now()
    #先删除,再写入
    entry1.delete(0,tkinter.END)
    time.sleep(0.1)
    #写入值
    entry1.insert(0,msg)




btn = tkinter.Button(win,text='登录',command=print_msg,width=100,bg='red')
btn.grid(row=2,column=0,columnspan=100)

qty = tkinter.Button(win,text='Quit',command = win.quit,bg='yellow',width=10,heigh=1,justify='center')
qty.grid(row=3,column=0,columnspan=100,)


win.mainloop()
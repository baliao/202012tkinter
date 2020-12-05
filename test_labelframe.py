#coding:utf-8
import tkinter

win= tkinter.Tk()
win.title('test label frame')
win.geometry('300x200')

fw = tkinter.LabelFrame(win,text='用户登录',width=100,height=15)

user_label = tkinter.Label(fw,text='姓名')
user_label.grid(row=0,column=0)

user_name = tkinter.StringVar()
user_entry = tkinter.Entry(fw,textvariable=user_name)
user_entry.grid(row=0,column=1)


passwd_label = tkinter.Label(fw,text='密码')
passwd_label.grid(row=1,column=0)

pass_word = tkinter.StringVar()
passwd_entry = tkinter.Entry(fw,textvariable=pass_word,show='*')
passwd_entry.grid(row=1,column=1)

def confirm():
    user = user_name.get()
    passwd = pass_word.get()
    print (user,passwd)


cnf_btn = tkinter.Button(fw,text='确认',command=confirm)
cnf_btn.grid(row=2,columnspan=10)




fw.pack()

win.mainloop()











win.mainloop()
#coding:utf-8
import tkinter
from tkinter import messagebox


win = tkinter.Tk()
win.title('全球信息中心')
win.geometry('500x200')

menubar = tkinter.Menu(win)
userinfobar = tkinter.Menu(menubar,tearoff=False)
menubar.add_cascade(menu=userinfobar,label='UserInfo',underline=0)
userinfobar.add_command(label='个人信息')
userinfobar.add_command(label='职业信息')


companyinfobar = tkinter.Menu(menubar,tearoff=False)
menubar.add_cascade(menu=companyinfobar,label='公司信息')
companyinfobar.add_command(label='电话',accelerator='Ctrl+n',underline=6)


areabar = tkinter.Menu(companyinfobar,tearoff=False)
areabar.add_command(label='中国区')
areabar.add_separator()
areabar.add_command(label='美国区')

companyinfobar.add_cascade(menu=areabar,label='地址',)

win.bind('<Control-n>',lambda event:messagebox.showinfo('New file','确认需要新建吗?'))


win.config(menu=menubar)


win.mainloop()

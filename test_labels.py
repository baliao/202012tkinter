#coding:utf-8
import tkinter
import tkinter.ttk as ttk

win = tkinter.Tk()
win.title('label 控制测试')
win.iconbitmap('icon.ico')
win.geometry('550x500')

#显示图片
html_gif = tkinter.PhotoImage(file = 'icon.gif')

#padx,pady 表示距控制左右上下边距,
#relief 控件表现形式,raised,solid,groove,flat
label1 = tkinter.Label(win,text='tkinter label widget....',
                       fg = 'red',bg='yellow',
                       height = 20,
                       width = 45,
                       relief = 'flat',
                       # padx = 5,
                       # pady =10,
                       # image = html_gif,
                       )
label1.pack()
sep = ttk.Separator(win,orient = tkinter.HORIZONTAL)
sep.pack(fill=tkinter.X,padx=5)
label2 = tkinter.Label(win,text='这是第二个label 控件',bg='green')
label2.pack()


#config 方法

win.mainloop()
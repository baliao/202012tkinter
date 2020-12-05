#coding:utf-8
import tkinter


win = tkinter.Tk()
win.title('第一个tk测试')
#获取屏幕的宽度和高度
dep = win.winfo_screenheight()
wid = win.winfo_screenwidth()
print (wid,dep)

#长宽 位置号,屏幕中央
win.geometry('250x200+%d+%d' %((wid-250)/2,(dep-200)/2))
# win.state('zoomed') #最大化窗口
# win.resizable(False,False) #是否可以更改窗口的大小/宽/高
win.config(bg='red') #窗口背景颜色


win.iconbitmap('icon.ico')
win.mainloop()

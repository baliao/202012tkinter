#coding:utf-8
import tkinter
import tkinter.ttk as ttk

win= tkinter.Tk()
win.title('label test2')
win.geometry('500x300')
lable1 = tkinter.Label(text='中国人民共和国',bg='red',)
lable2 = tkinter.Label(text='美利坚合众国',bg='yellow')
lable3 = tkinter.Label(text='台湾香港澳门',bg='green')

# lable1.pack(side=tkinter.BOTTOM)
# lable2.pack(side=tkinter.BOTTOM)
# lable3.pack(side=tkinter.BOTTOM)

#side 属性水平或垂直配置控件,side = LEFT,RIGHT,BOTTOM,TOP
# padx pady 边界距离
#ipax,ipady 控制标签内文字与控件边界的距离
#anchor 表示在窗口中的位置
#fill 表示填充方向

#fill=tkinter.X 填充X 轴,pady =2 距上面为2
lable1.pack(fill=tkinter.X,pady=2)
lable2.pack(pady=3)
lable3.pack(pady=10,fill = tkinter.X)


# grid 参数 row,column,padx,pady,rowspan,columnspan,
# place 方法, height,width,

win.mainloop()



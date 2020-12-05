#coding:utf-8
import tkinter

win=tkinter.Tk()
win.title('单选')
win.geometry('300x200')
label = tkinter.Label(win,text='预设值',bg='green',width=100)
label.pack()

# var= tkinter.IntVar()
# var.set(1)

# def show():
#     number = var.get()
#
#     if number ==1:
#         label.config(text='选择了男生')
#         msg = '点了我,男'
#     else:
#         label.config(text='选择了女生')
#         msg = '点了我,女'

#value 选项按键的值
#text 按钮旁边的文字
#textvarible 以变量方式显示选项按钮文字
# variable 设置或取得目前选取的单选按钮,值的类型为IntVar StringVar,跟踪radiobuton状态

# radioman = tkinter.Radiobutton(win,text='男生',variable=var,value=1,command=show,selectcolor='red')
# radioman.pack()
#
# radiowoman = tkinter.Radiobutton(win,text='女生',variable=var,value=2,command=show)
# radiowoman.pack()
#
# msg = tkinter.StringVar()
#
# radioit = tkinter.Radiobutton(win,variable=msg,value=3,command=show)
# radioit.pack()

def pprint():
    name = var1.get()
    print ("选择的城市为:{!r}".format(name))


cities = {0:'北京',1:'上海',2:'深圳',3:'广州'}

var1 = tkinter.StringVar()
# var1.set(-1)

for var,city in cities.items():
    tkinter.Radiobutton(win,text=city,variable=var1,value=city,command=pprint ,indicator =0 ).pack()

win.mainloop()
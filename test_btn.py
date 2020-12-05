#coding:utf-8
import tkinter
import tkinter.ttk as ttk
import time,datetime

win = tkinter.Tk()
win.title('btn 测试中')
win.geometry('300x200')
label = tkinter.Label(win,text='')
label.pack()

# def print():
#
#     label['bg'] = 'yellow'
#     label['fg'] = 'blue'
#     while True:
#         msg = datetime.datetime.now()
#         label['text'] = '打印内容区域:{}'.format(msg)
#         label.update()
#         time.sleep(1)

def print():
    label.config(text='文字打印测试开始....',bg='red',fg='blue')



btn = tkinter.Button(win,text='打印测试中',command=print)
btn.pack()
win.mainloop()
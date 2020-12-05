#coding:utf-8
import tkinter
win = tkinter.Tk()
win.title('panel test')

pw= tkinter.PanedWindow(orient=tkinter.HORIZONTAL)
leftfrme = tkinter.LabelFrame(pw,text='Left',width=100,height=150)
pw.add(leftfrme,weight=2)

midfrme = tkinter.LabelFrame(pw,text='Mide',width=100,height=150)
pw.add(midfrme,weight=2)
btn = tkinter.Button(midfrme,text='确认',bg='red',width=10,height=2,padx=5,pady=5)
btn.pack()

bottom = tkinter.LabelFrame(pw,text='Bottom',width=100,height=150)
pw.add(bottom,weight=1)

pw.pack(fill=tkinter.BOTH,expand=True,padx=10,pady=10)
win.mainloop()
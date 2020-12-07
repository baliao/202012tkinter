#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os, sys
import requests, json

try:
    from tkinter import *
except ImportError:  # Python 2.x
    PythonVersion = 2
    from Tkinter import *
    from tkFont import Font
    from ttk import *
    # Usage:showinfo/warning/error,askquestion/okcancel/yesno/retrycancel
    from tkMessageBox import *
    # Usage:f=tkFileDialog.askopenfilename(initialdir='E:/Python')
    # import tkFileDialog
    # import tkSimpleDialog
else:  # Python 3.x
    PythonVersion = 3
    from tkinter.font import Font
    from tkinter.ttk import *
    from tkinter.messagebox import *
    # import tkinter.filedialog as tkFileDialog
    # import tkinter.simpledialog as tkSimpleDialog    #askstring()


class Application_ui(Frame):
    # 这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title(u'翻译器')
        self.master.geometry('324x146')
        self.master.resizable(0, 0)
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.Text2Var = StringVar(value='')
        self.Text2 = Text(self.top)
        self.Text2.place(relx=0.519, rely=0.329, relwidth=0.423, relheight=0.5)
        gComps['t2'] = self.Text2

        self.Text1Var = StringVar(value='')
        self.Text1 = Text(self.top)
        self.Text1.place(relx=0.049, rely=0.329, relwidth=0.423, relheight=0.5)
        gComps['t1'] = self.Text1

        self.style.configure('Label1.TLabel', anchor='w')
        self.Label1 = Label(self.top, text=u'请输入要翻译的内容：', style='Label1.TLabel')
        self.Label1.place(relx=0.074, rely=0.164, relwidth=0.398, relheight=0.116)

        self.Command1 = Button(self.top, text=u'翻  译', command=self.Command1_Cmd)
        self.Command1.place(relx=0.593, rely=0.164, relwidth=0.299, relheight=0.116)


class Application(Application_ui):
    # 这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)

    def Command1_Cmd(self, event=None):
        txt = gComps['t1'].get(1.0, END)
        translation = self.translate(txt)
        gComps['t2'].delete(1.0, END)
        gComps['t2'].insert(1.0, translation)

    def translate(self, txt=''):
        url = 'http://fy.iciba.com/ajax.php?a=fy'
        req = requests.Session()
        head = {'User-Agent': "Mozilla/5.0 (Windows NT 5.1; rv:52.0) Gecko/20100101 Firefox/52.0"}
        data = {'f': 'auto', 't': 'auto', 'w': txt}
        res = req.post(url, data=data, headers=head)
        result = json.loads(res.text)
        try:
            out = result['content']['out']
        except:
            out = '\n'.join(result['content']['word_mean'])
        try:
            out = out.replace('<br/>', '\n')
        except:
            pass
        return out


gComps = {}

if __name__ == "__main__":
    top = Tk()
    b=Application(top)
    b.master.title('我的英语翻译')
    b.master.geometry('600x400')
    b.master.iconbitmap('icon.ico')
    b=mainloop()
    try:
        top.destroy()
    except:
        pass

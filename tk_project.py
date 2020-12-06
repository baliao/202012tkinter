#coding:utf-8
import os, sys
from tkinter.font import Font
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *


class Application_ui(Frame):

    # 这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def init(self, master=None):
        Frame.__init__(self, master)
        self.master.title('海港高桩码头结构安全评估及预警平台')
        self.master.geometry('808x447')
        self.createWidgets()


    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()


        # 主菜单
        self.MainMenu = Menu(self.top, tearoff=0)
        self.top['menu'] = self.MainMenu

        self.Sysmenu = Menu(self.MainMenu, tearoff=0)
        self.MainMenu.add_cascade(menu=self.Sysmenu, label='主菜单[M]', underline=4)
        self.Choose_project = Menu(self.Sysmenu, tearoff=0)
        self.Sysmenu.add_cascade(menu=self.Choose_project, label='选择工程')
        self.Choose_project.add_command(label='天津港南疆27#通用码头工程', command=self.My_project_Cmd)
        self.Choose_project.add_command(label='其它', state='disabled', command=self.Other_project_Cmd)

        self.Sysmenu.add_command(label='返回主界面', accelerator='Ctrl-B', command=self.Return_mainform_Cmd)
        self.top.bind_all('<Control-B>', self.Return_mainform_Cmd)
        self.top.bind_all('<Control-b>', self.Return_mainform_Cmd)

        self.Sysmenu.add_command(label='退出程序[X]', accelerator='Ctrl-X', command=self.Exit_program_Cmd)
        self.top.bind_all('<Control-X>', self.Exit_program_Cmd)
        self.top.bind_all('<Control-x>', self.Exit_program_Cmd)
        # 安全评估

        self.Safe_assess = Menu(self.MainMenu, tearoff=0)
        self.MainMenu.add_cascade(menu=self.Safe_assess, label='安全评估[A]', state='disabled', underline=5)

        self.Safe_assess.add_command(label='码头结构示意图', accelerator='Ctrl-P', command=self.Show_picture_Cmd)
        self.top.bind_all('<Control-P>', self.Show_picture_Cmd)
        self.top.bind_all('<Control-p>', self.Show_picture_Cmd)

        self.Safe_assess.add_command(label='码头结构安全评估', accelerator='Ctrl-M', command=self.My_assess_Cmd)
        self.top.bind_all('<Control-M>', self.My_assess_Cmd)
        self.top.bind_all('<Control-m>', self.My_assess_Cmd)
        #预警系统
        self.Warn_sys = Menu(self.MainMenu, tearoff=0)
        self.MainMenu.add_cascade(menu=self.Warn_sys, label='预警系统[W]', state='disabled', underline=5)

        self.Warn_sys.add_command(label='码头结构安全预警', accelerator='Ctrl-J', command=self.Warn_wharf_Cmd)
        self.top.bind_all('<Control-J>', self.Warn_wharf_Cmd)
        self.top.bind_all('<Control-j>', self.Warn_wharf_Cmd)
        self.Warn_sys.add_command(label='岸坡安全预警', accelerator='Ctrl-O', command=self.Warn_slope_Cmd)
        self.top.bind_all('<Control-O>', self.Warn_slope_Cmd)
        self.top.bind_all('<Control-o>', self.Warn_slope_Cmd)
        # 安全日志及帮助
        self.MainMenu.add_command(label='安全日志[L]', underline=5, command=self.Safe_log_Cmd)
        self.MainMenu.add_command(label='帮助[H]', underline=3, command=self.My_help_Cmd)

class Application(Application_ui):
    def __init__(self, master=None):
        Application_ui.__init__(self, master)


    def My_project_Cmd(self, event=None):
        pass


    def Other_project_Cmd(self, event=None):
        # TODO, Please finish the function here!
        pass


    def Return_mainform_Cmd(self, event=None):
        # TODO, Please finish the function here!
        pass


    def Exit_program_Cmd(self, event=None):
        # TODO, Please finish the function here!
        pass


    def Show_picture_Cmd(self, event=None):
        # TODO, Please finish the function here!
        pass


    def My_assess_Cmd(self, event=None):
        # TODO, Please finish the function here!
        pass


    def Warn_wharf_Cmd(self, event=None):
        # TODO, Please finish the function here!
        pass


    def Warn_slope_Cmd(self, event=None):
        # TODO, Please finish the function here!
        pass


    def Safe_log_Cmd(self, event=None):
        # TODO, Please finish the function here!
        pass


    def My_help_Cmd(self, event=None):
        # TODO, Please finish the function here!
        pass


app = Application()
app.mainloop()
#coding:utf-8

import tkinter

win = tkinter.Tk()
win.title('Release RM V01')
dep = win.winfo_screenheight()
wid = win.winfo_screenwidth()
win.geometry('%dx%d+%d+%d' %(wid/2,dep/2,wid/5,dep/5))

machine_list = ['Choose Machine','fxcapp1134','fxcapp1089','fxcapp1088','fxcapp837']
side_list = ['Right or Left ?','leftchass','rightchass']
port_list = ['Port number ?','port_0','port_1','port_2']

var_machine = tkinter.StringVar()
client_frame = tkinter.LabelFrame(win,text='Cilent Info',width=300,height=100)
client_frame.pack()
optionmenu_machine = tkinter.OptionMenu(client_frame,var_machine,*machine_list,)
var_machine.set(machine_list[0])
optionmenu_machine.pack(side=tkinter.LEFT)


var_side = tkinter.StringVar()
optionmenu_side = tkinter.OptionMenu(client_frame,var_side,*side_list,)
var_side.set(side_list[0])
optionmenu_side.pack(side=tkinter.LEFT)

var_port = tkinter.StringVar()
optionmenu_port = tkinter.OptionMenu(client_frame,var_port,*port_list,)
var_port.set(port_list[0])
optionmenu_port.pack(side=tkinter.LEFT)


summary_labelframe = tkinter.LabelFrame(win,text='User Input',width=300,height=100)
summary_labelframe.pack()
client_info = tkinter.StringVar()
client_info_label = tkinter.Label(summary_labelframe,text='Client Info:',textvariable=client_info,height=5,width=300)
client_info_label.pack()
def summary():
    machine = var_machine.get()
    side = var_side.get()
    port = var_port.get()
    msg = '{}-{}-{}'.format(machine,side,port)
    client_info.set(msg)
    client_info_label.config(bg='red')


def cancel():
    client_info.set('')
    client_info_label.config(bg='white')

def request_rm():
    msg = client_info.get()
    msg += 'Request --->'
    client_info.set(msg)


def release_rm():
    msg = client_info.get()
    msg += 'release --->'
    client_info.set(msg)
    pass




action_labelframe = tkinter.LabelFrame(win,text='Action For RM',width=300,height=100)
action_labelframe.pack(side=tkinter.LEFT)
request_btn = tkinter.Button(action_labelframe,text='Request',bg='blue',command=request_rm,width=50,height=5)
request_btn.pack()

release_btn = tkinter.Button(action_labelframe,text='Release',bg='orange',command=release_rm,width=50,height=5)
release_btn.pack()


confirm_labelframe = tkinter.LabelFrame(win,text='User to Confirm to do ',width=300,height=100)
confirm_labelframe.pack(side=tkinter.RIGHT)
confirm_btn = tkinter.Button(confirm_labelframe,text='Confirm',bg='green',command=summary,width=50,height=5)
confirm_btn.pack()

cancel_btn = tkinter.Button(confirm_labelframe,text='Cancel',bg='yellow',command=cancel,width=50,height=5)
cancel_btn.pack()




win.mainloop()
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk  # 使用Tkinter前需要先导入
import tkinter.filedialog
# 第1步，实例化object，建立窗口window
window = tk.Tk()
# 第2步，给窗口的可视化起名字
window.title('Environment Detection tool - version 1.0')
# 第3步，设定窗口的大小(长 * 宽)
window.geometry('500x300')  # 这里的乘是小x


# 第4步，在图形界面上设定标签
var = tk.StringVar()  # 将label标签的内容设置为字符类型，用var来接收hit_me函数的传出内容用以显示在标签上
show_inf = tk.Label(window, textvariable=var, bg='green', fg='white', font=('Arial', 12), width=50, height=10)
# 说明： bg为背景，fg为字体颜色，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高
show_inf.pack()

# 定义一个函数功能（内容自己自由编写），供点击Button按键时调用，调用命令参数command=函数名
on_hit = False


def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('you hit meh')

    else:
        on_hit = False
        var.set('')


def Load_scfc_file():
    a = tkinter.filedialog.asksaveasfilename()#返回文件名
    print(a)
    a = tkinter.filedialog.asksaveasfile()#会创建文件
    print(a)
    a = tkinter.filedialog.askopenfilename()#返回文件名
    print(a)
    a = tkinter.filedialog.askopenfile()#返回文件流对象
    print(a)
    a = tkinter.filedialog.askdirectory()#返回目录名
    print(a)
    a = tkinter.filedialog.askopenfilenames()#可以返回多个文件名
    print(a)
    a = tkinter.filedialog.askopenfiles()#多个文件流对象
    print(a)


# 第5步，在窗口界面设置放置Button按键
b = tk.Button(window, text='导入sfc文件', font=('Arial', 12), width=10, height=1, command=Load_scfc_file)
b.place(x="30", y='200')
c = tk.Button(window, text='开始检测', font=('Arial', 12), width=10, height=1, command=hit_me)
c.place(x="140", y='200')

# 第6步，主窗口循环显示
window.mainloop()
import tkinter as tk
import io, os, sys
import win32print
import win32api

from tkinter import *
from tkinter import font # * doesn't import font


huan= tk.Tk()
huan.title('打印贴纸 v1.0')

#创建一个800*500的画布
canvas1 = tk.Canvas(huan, width = 800, height = 500, relief = 'raised')
canvas1.pack()

entry1 = tk.Entry(huan, width=40, font=('Arial 24'))
canvas1.create_window(400, 100, window=entry1)

def font_size(fs):
    return font.Font(family='Helvetica', size=fs, weight='bold')

def gethuanhuo():  
    x1 = entry1.get()

    huanhuo = "Date 类型 Tracking Order_Number UPC 包装箱SN 电脑SN Notes".split()
    list= x1.split()
    dic = {huanhuo[i]: list[i] for i in range(len(huanhuo))}
    fake_file = io.StringIO()
    for key, value in dic.items():
        print(key, ":", value, end="\n", file=fake_file)
    msg = tk.Label(huan, text= fake_file.getvalue())  #fake_file.getvalue()换行后显示在画布上
    msg.config(bg='lightgreen', font=('times', 18))
    msg.pack()
    
    myText = open(r'.\huanhuo.txt','w', encoding='utf-8')
    myList= []
    for key, value in dic.items():
        myList.append(key + ': ' + value)
    for i in myList:
        myText.write(i + '\n')
    myText.close()

    printer_name = win32print.GetDefaultPrinter()
    hPrinter = win32print.OpenPrinter(printer_name)
    win32api.ShellExecute(0, "print", r'.\huanhuo.txt', '/d:"%s"' % printer_name, ".", 0)
    
def getwalmart():  
    x1 = entry1.get()

    walmart = "Date Tracking Order_Number RMA_No UPC 包装箱SN 电脑SN Notes".split()
    list= x1.split()
    dic = {walmart[i]: list[i] for i in range(len(walmart))}
    fake_file = io.StringIO()
    for key, value in dic.items():
        print(key, ":", value, end="\n", file=fake_file)
    msg = tk.Label(huan, text= fake_file.getvalue())
    msg.config(bg='lightgreen', font=('times', 18))
    msg.pack()

    myText = open(r'.\huanhuo.txt','w', encoding='utf-8')
    myList= []
    for key, value in dic.items():
        myList.append(key + ': ' + value)
    for i in myList:
        myText.write(i + '\n')
    myText.close()

    printer_name = win32print.GetDefaultPrinter()
    hPrinter = win32print.OpenPrinter(printer_name)
    win32api.ShellExecute(0, "print", r'.\huanhuo.txt', '/d:"%s"' % printer_name, ".", 0)

def getnewegg():  
    x1 = entry1.get()

    newegg = "Date Tracking Order_Number RMA_No UPC 包装箱SN 电脑SN Notes".split()
    list= x1.split()
    dic = {newegg[i]: list[i] for i in range(len(newegg))}
    fake_file = io.StringIO()
    for key, value in dic.items():
        print(key, ":", value, end="\n", file=fake_file)
    msg = tk.Label(huan, text= fake_file.getvalue())
    msg.config(bg='lightgreen', font=('times', 18))
    msg.pack()
    

    myText = open(r'.\huanhuo.txt','w', encoding='utf-8')
    myList= []
    for key, value in dic.items():
        myList.append(key + ': ' + value)
    for i in myList:
        myText.write(i + '\n')
    myText.close()

    printer_name = win32print.GetDefaultPrinter()
    hPrinter = win32print.OpenPrinter(printer_name)
    win32api.ShellExecute(0, "print", r'.\huanhuo.txt', '/d:"%s"' % printer_name, ".", 0)

def getrenew():  
    x1 = entry1.get()

    renew = "日期 Tracking 订单号 商品名称 箱子UPC	箱子SN 电脑SN 处理".split()
    list= x1.split()
    dic = {renew[i]: list[i] for i in range(len(renew))}
    fake_file = io.StringIO()
    for key, value in dic.items():
        print(key, ":", value, end="\n", file=fake_file)
    msg = tk.Label(huan, text= fake_file.getvalue())
    msg.config(bg='lightgreen', font=('times', 18))
    msg.pack()
    

    myText = open(r'.\huanhuo.txt','w', encoding='utf-8')
    myList= []
    for key, value in dic.items():
        myList.append(key + ': ' + value)
    for i in myList:
        myText.write(i + '\n')
    myText.close()

    printer_name = win32print.GetDefaultPrinter()
    hPrinter = win32print.OpenPrinter(printer_name)
    win32api.ShellExecute(0, "print", r'.\huanhuo.txt', '/d:"%s"' % printer_name, ".", 0)
    
button1 = tk.Button(text='换货或未申请退货', command=gethuanhuo)
button1['font'] = font_size(15)
canvas1.create_window(400, 180, window=button1)

button2 = tk.Button(text='Walmart', command=getwalmart)
button2['font'] = font_size(15)
canvas1.create_window(400, 240, window=button2)

button3 = tk.Button(text='Newegg', command=getnewegg)
button3['font'] = font_size(15)
canvas1.create_window(400, 300, window=button3)

button4 = tk.Button(text='Renew', command=getrenew)
button4['font'] = font_size(15)
canvas1.create_window(400, 360, window=button4)

huan.mainloop()

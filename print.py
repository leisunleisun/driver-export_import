import tkinter as tk
import io
import os, sys
import win32print
import win32api

hPrinter = win32print.OpenPrinter('ZDesigner GK420d')
printer_name = win32print.GetDefaultPrinter()

huan= tk.Tk()
huan.title('打印贴纸')

canvas1 = tk.Canvas(huan, width = 800, height = 400, relief = 'raised')
canvas1.pack()

entry1 = tk.Entry(huan)
canvas1.create_window(400, 140, window=entry1)


def gethuanhuo():  
    x1 = entry1.get()

    huanhuo = "Date 类型 Tracking Order_Number UPC 包装箱SN 电脑SN Notes".split()
    list= x1.split()
    dic = {huanhuo[i]: list[i] for i in range(len(huanhuo))}
    fake_file = io.StringIO()
    for key, value in dic.items():
        print(key, ":", value, end="\n", file=fake_file)
    raw_data = bytes(fake_file.getvalue(), "utf-8")


    
    msg = tk.Label(huan, text= fake_file.getvalue())
    msg.config(bg='lightgreen', font=('times', 18))
    msg.pack()

    win32api.ShellExecute(0, "print", raw_data, '/d:"%s"' % printer_name, ".", 0)
    
    try:
        hJob = win32print.StartDocPrinter(hPrinter, 1, ("test of raw data", None, "RAW"))
        try:
            win32print.StartPagePrinter(hPrinter)
            win32print.WritePrinter(hPrinter, raw_data)
            win32print.EndPagePrinter(hPrinter)
        finally:
            win32print.EndDocPrinter(hPrinter)
    finally:
        win32print.ClosePrinter(hPrinter)
    
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

    #label1 = tk.Label(huan, text= fake_file.getvalue())
    #canvas1.create_window(400, 500, window=label1)

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
    
        
button1 = tk.Button(text='换货或未申请退货', command=gethuanhuo)
canvas1.create_window(400, 180, window=button1)

button2 = tk.Button(text='Walmart', command=getwalmart)
canvas1.create_window(400, 220, window=button2)

button3 = tk.Button(text='Newegg', command=getnewegg)
canvas1.create_window(400, 260, window=button3)

huan.mainloop()

import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.title("Kahn Software v1")  # #窗口标题
win.geometry("600x500+200+20")  #

tree = ttk.Treeview(win)      # #创建表格对象
tree["columns"] = ("姓名", "年龄", "身高", "体重")     # #定义列
tree.column("姓名", width=100)          # #设置列
tree.column("年龄", width=100)
tree.column("身高", width=100)
tree.column("体重", width=100)
tree.heading("姓名", text="x姓名")        # #设置显示的表头名
tree.heading("年龄", text="x年龄")
tree.heading("身高", text="x身高")
tree.heading("体重", text="x体重")
tree.insert("", 0, text="line1", values=("卡恩", "18", "180", "65"))    # #给第0行添加数据，索引值可重复
tree.insert("", 1, text="line2", values=("范冰冰", "38", "170", "55"))
tree.insert("", 2, text="line3", values=("戚薇", "28", "169", "50"))
tree.insert("", 3, text="line4", values=("杨霞", "30", "172", "63"))
tree.insert("", 4, text="line5", values=("李小冉", "31", "175", "65"))
tree.insert("", 5, text="line6", values=("迪丽热巴", "29", "175", "61"))

tree.pack()
win.mainloop()   #
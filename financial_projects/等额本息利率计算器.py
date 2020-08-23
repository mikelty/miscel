import tkinter as tk
from tkinter import messagebox
from utils import calc_interest

root=tk.Tk()
root.title('等额本息利率计算器')

var_names=['本金','还钱总数','周期数']
defaults=[45,107,7]
data=[0.0 for _ in range(len(var_names))]
for r,(var,val) in enumerate(zip(var_names,defaults)):
	label=tk.Label(text=var,width=25)
	label.grid(row=r,column=0)
	data[r]=tk.DoubleVar(value=defaults[r])
	entry=tk.Entry(fg="white",bg="grey",width=50,textvariable=data[r])
	entry.grid(row=r,column=1)

def on_submit():
	global 本金,还钱总数,周期数
	本金 = data[0].get()
	还钱总数 = data[1].get()
	周期数 = int(data[2].get())
	interest=calc_interest(本金,还钱总数,周期数)
	messagebox.showinfo("周期利率",str(round(interest,2))+'%') #27.9

submit=tk.Button(root,text="提交",command=on_submit)
submit.grid(row=len(var_names),column=1)
root.mainloop()
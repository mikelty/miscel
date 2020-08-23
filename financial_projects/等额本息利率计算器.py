#20-40
import tkinter as tk
from tkinter import messagebox
from utils import calc_interest
from plot_interest_investment import plot_varying_funds

root=tk.Tk()
root.title('等额本息利率计算器')
inputs=tk.Frame(root)
inputs.pack(side=tk.BOTTOM)

var_names, defaults = [], []
sel,CALC_MODE,PLOT_MODE=tk.IntVar(inputs),0,1

def on_submit():
	global 本金,还钱总数,周期数,data
	if sel.get()==CALC_MODE:
		interest=calc_interest(data[0].get(),data[1].get(),int(data[2].get()))
		messagebox.showinfo("周期利率",str(round(interest,2))+'%') #27.9
	else:
		plot_varying_funds(data[0].get(),data[1].get(),data[2].get(),int(data[3].get()))

def sel_mode():
	global data,inputs
	inputs.destroy()
	inputs=tk.Frame(root)
	inputs.pack(side=tk.BOTTOM)
	if sel.get() == CALC_MODE:

		var_names=['本金']
		defaults=[45]
	else:
		var_names=['最低本金','最高本金']
		defaults=[25,45]
	var_names=var_names+['还钱总数','周期数']
	defaults=defaults+[107,7]
	data=[0.0 for _ in range(len(var_names))]
	for r,(var,val) in enumerate(zip(var_names,defaults)):
		label=tk.Label(inputs,text=var,width=25)
		label.grid(row=r,column=0)
		data[r]=tk.DoubleVar(inputs,value=defaults[r])
		entry=tk.Entry(inputs,fg="white",bg="grey",width=50,textvariable=data[r])
		entry.grid(row=r,column=1)

	submit=tk.Button(inputs,text="提交",command=on_submit)
	submit.grid(row=len(var_names),column=1)

select=tk.Frame(root)
select.pack(side=tk.TOP)
calc_mode=tk.Radiobutton(select,text='计算周期利率（默认）',variable=sel,value=CALC_MODE,command=sel_mode)
calc_mode.grid(row=0,column=0)
calc_mode.invoke()
plot_mode=tk.Radiobutton(select,text='绘制不同本金的周期利率',variable=sel,value=PLOT_MODE,command=sel_mode)
plot_mode.grid(row=0,column=1)



root.mainloop()
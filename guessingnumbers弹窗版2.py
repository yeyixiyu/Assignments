import tkinter as tk
from tkinter import messagebox
import random

count=0#Global Variable
def generate_random_number():
    ware = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return int(''.join(map(str, random.sample(ware, 4)[:])))

def check_number():
    player_input = entry.get()
    if (len(player_input) != 4 or not player_input.isdigit() or len(player_input)
            != len(set(player_input))):
        messagebox.showerror('错误', '请输入一个正确的四位数！')
        entry.delete(0, tk.END)
        return
    a = 0
    b = 0
    for i in range(0, 4, 1):
        if player_input[i] == '0':
            messagebox.showerror('错误', '请输入一个正确的四位数！')
            entry.delete(0, tk.END)
            return
        if player_input[i] == str(generated_number)[i]:
            a += 1
        for j in range(0, 4, 1):
            if player_input[i] == str(generated_number)[j]:
                b += 1
    b -= a
    entry.delete(0, tk.END)
    global count
    count += 1
    if int(player_input) == generated_number:
        if count <10:
            messagebox.showinfo('恭喜',f'''您猜对了！数字是{generated_number}
                            您只用了{count}次就猜出来了！''')
            tx.insert(tk.END,player_input+f'    {count}次')
        else:
            messagebox.showinfo('失败', '别灰心，点击重新开始再来一次吧')
    else:
        if count <10:
            messagebox.showerror('很遗憾',f'''您猜错了，还剩下{(10 - count)}次机会
      本次的结果是{a}A{b}B''')
            tx.insert(tk.END,player_input+f'    {a}A{b}B')
        else:
            messagebox.showinfo('失败', '您输了，正确数字是{}'.format(generated_number))
            tx.insert(tk.END, player_input+' 正确数字是{}'.format(generated_number))

def regain_number():
    global count
    count=0
    global generated_number
    generated_number = generate_random_number()
    tx.delete(0,tk.END)

if __name__ == '__main__':
    generated_number = generate_random_number()

    app = tk.Tk()
    app.title('猜数游戏')
    app.geometry('750x640')

    rule = tk.Label(app, text=
''' 规则：数字和位置均一致计为一个A，
含有某个数字但位置不对计为一个B，
 请输入一个四位数字互不相同且不为0的四位数:'''
                    ,width=45,height=4,font=("黑体", 25))
    rule.pack()
    entry = tk.Entry(app,width=5,font=('黑体', 40))
    entry.pack()
    whiteland = tk.Label(app, width=40, height=1)
    whiteland.pack()

    button = tk.Button(app,text='猜测',font=('黑体',20), command=check_number)
    button.pack()
    whiteland2 = tk.Label(app, width=40, height=1)
    whiteland2.pack()

    tx=tk.Listbox(app,font=12)
    tx.pack()
    whiteland3 = tk.Label(app, width=40, height=1)
    whiteland3.pack()
    button = tk.Button(app, text='重新开始', font=('黑体', 20), command=regain_number)
    button.pack()

    app.mainloop()
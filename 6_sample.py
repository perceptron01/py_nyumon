# チェックボックスの表示
import tkinter as tk
base = tk.Tk()
fruites = {0:"りんご", 1:"みかん", 2:"バナナ", 3:"夏みかん", 4:"ぶどう"}

check_value = {}
for i in range(len(fruites)):
    check_value[i] = tk.BooleanVar()
    tk.Checkbutton(base, variable = check_value[i], text = fruites[i]).pack(anchor = tk.W)

def buy():
    for i in check_value:
        if check_value[i].get() == True:
            print(fruites[i])

tk.Button(base, text = '購入する', command = buy).pack()


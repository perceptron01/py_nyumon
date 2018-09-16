import tkinter as tk 

base = tk.Tk()
string = tk.StringVar() # 文字列を扱えるように
entry = tk.Entry(base, textvariable = string).pack() # 入力フォームを作成
label = tk.Label(base, textvariable = string).pack() # ラベルの作成
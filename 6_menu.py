import tkinter as tk 

base = tk.Tk()

def supermode():
    print('super mode!')

menubar = tk.Menu(base) # メニューバーの項目を置く場所
filemenu = tk.Menu(menubar)
filemenu.add_command(label = 'supermode', command = supermode) # クリックしたときに表示される項目を追加
menubar.add_cascade(label = 'Operation', menu = filemenu)
base.config(menu = menubar)

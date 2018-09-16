import tkinter as tk
import tkinter.messagebox as msg

base = tk.Tk() # window起動
base.withdraw() # windowを隠す

response = msg.askyesno("Warinig!", "Are you alright?")

if (response == True):
    print("OK!")
else:
    print("HELP!")



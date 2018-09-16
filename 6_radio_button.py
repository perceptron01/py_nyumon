import tkinter as tk

base = tk.Tk()
radio_value = tk.IntVar()
radio_value.set(1)
lunch = {0: "寿司", 1: "海鮮丼", 2:"うな重"}

for i in range(len(lunch)):
    tk.Radiobutton(text = lunch[i], variable = radio_value, value = i).pack()

def buy():
    value = radio_value.get()
    print(lunch[value])

tk.Button(base, text = "購入する", command = buy).pack()
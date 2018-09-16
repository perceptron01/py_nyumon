import qrcode as qr
import tkinter as tk 
import tkinter.filedialog as fd 
from PIL import ImageTk

base = tk.Tk()
base.title('QRcode Generator')
input_area = tk.Frame(base, relief = tk.RAISED, bd = 2)
image_area = tk.Frame(base, relief = tk.SUNKEN, bd = 2)
encode_text = tk.StringVar()
entry = tk.Entry(input_area,  textvariable = encode_text).pack(side = tk.LEFT)
qr_label = tk.Label(image_area)

def generate():
    # executed when generate button is pushed
    qr_label.qr_img = qr.make(encode_text.get())
    img_widh, img_height = qr_label.qr_img.size
    
    qr_label.tk_image = ImageTk.PhotoImage(qr_label.qr_img)
    
    qr_label.config(
        image = qr_label.tk_image, 
        width = img_widh, 
        height = img_height
    )
    qr_label.pack()

# ボタンを作成
encode_buttom = tk.Button(
    input_area, 
    text = 'generate QR Code!', 
    command = generate
    ).pack(side = tk.LEFT)

# フレームの表示
input_area.pack(pady = 5) # 入力欄とボタンフレーム＋余白サイズ
image_area.pack(padx = 3, pady = 1)  # QRコード画像のフレーム外＋余白サイズ

def save():
    # メニューの作成
    filename = fd.asksaveasfilename(
        title = 'QRコードに名前をつけて保存する', initialfile = 'qrcode.png')
    if filename and hasattr(qr_label, 'qr_img'):
        qr_label.qr_img.save(filename)

def exit():
    base.destroy()

menubar = tk.Menu(base)
filemenu = tk.Menu(menubar)
menubar.add_cascade(label = 'File', menu = filemenu)
filemenu.add_command(label = 'save', command = save)
filemenu.add_separator()
filemenu.add_command(label = 'exit', command = exit)

base.config(menu = menubar)
base.mainloop()


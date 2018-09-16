import qrcode
encode_text = 'https://www.google.co.jp/'
img = qrcode.make(encode_text)
type(img)
img.show()
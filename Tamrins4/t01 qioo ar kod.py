import qrcode

name = input("Name khod ra vared konid: ")
family = input("Name khanevadegie khod ra vared konid: ")
cell_number = input("Shomare bede: ")

data = name + family + cell_number
img = qrcode.make(data)

img.save("qr.png")

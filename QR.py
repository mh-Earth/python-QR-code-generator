import qrcode
from tkinter import *
from tkinter.filedialog import asksaveasfilename

def get_QR():
    qr = qrcode.QRCode(
        version=1,#mini version=1,max=15
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=100,
        border=4,
    )
    qr.add_data(var.get())
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white") #you can give any color
    save=asksaveasfilename(defaultextension='.jpg', filetypes=[(".jpg", '*.jpg')],
                title="Choose filename")
    img.save(save)

if __name__ == "__main__":
        
    root=Tk()
    root.geometry("500x500")
    root.title("QR code generator")
    lable=Label(root,text="Enter the data for QR code").pack()
    var=StringVar()
    entry=Entry(root,textvariable=var).pack(ipadx=50)
    button=Button(root,text="GET QR CODE",command=get_QR).pack()


    root.mainloop()




































































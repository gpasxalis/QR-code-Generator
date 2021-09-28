from tkinter import*
from tkinter import messagebox
import os
import sys
import pyqrcode


def create_qr_code():
    if len(Subject.get()) != 0:
        global qr, photo, photo_display
        qr = pyqrcode.create(Subject.get())
        qrImage = qr.xbm(scale=9)
        photo_display = BitmapImage(data=qr.xbm(scale=6))
        photo = BitmapImage(data=qrImage)
        msg = 'QR Generated Successfully!'
        lbl_msg.config(text=msg)
    try:
        showcode()
    except:
        pass

def showcode():
    qr_code = Label(qr_Frame, bg='white', fg='white')
    qr_code.place(x=35, y=100, width=180, height=180)
    qr_code.config(image=photo_display)


def save_qr_code():
    dir = os.getcwd() + "\\QR Codes"
    if not os.path.exists(dir):
        os.makedirs(dir)
    try:
        if len(name.get()) != 0:
            qrImage = qr.png(os.path.join(dir, name.get()+".png"), scale=9)
            msg = 'QR Saved Successfully!'
            lbl_msg.config(text=msg)
        else:
            messagebox.showinfo("QR Generator", "Please enter a File Name")
    except:
        messagebox.showinfo("QR Generator", "Generate the QR code first!")


def clear_fields():
    SubEntry.delete(0, 'end')
    FileNameEntry.delete(0, 'end')
    qr_code = Label(qr_Frame, text='No QR\nAvailable', font=("times new roman", 15), bg='#053246', fg='white')
    qr_code.place(x=35, y=100, width=180, height=180)
    lbl_msg.config(text='')


if __name__ == "__main__":
    root = Tk()
    root.geometry("900x600+200+50")
    root.title("QR Generator | Developed by gpasxalis")
    root.resizable(False, False)

    ################################################################ MAIN FRAME ################################################################

    title = Label(root, text="QR Code Generator", font=("times new roman", 28), bg='#053246', fg='white').place(x=0, y=0, relwidth=1)
    mainFrame = Frame(root, bd=2, relief=RIDGE, bg='white')
    mainFrame.place(x=50, y=150, width=500, height=380)
    mainTitle = Label(mainFrame, text="Input Fields", font=("times new roman", 18), bg='#053246', fg='white').place(x=0, y=0, relwidth=1)

    ################################################################ MAIN FRAME ################################################################

    ############################################################### ENTRY FIELDS ###############################################################

    Sub = Label(mainFrame, text="Enter text", font=(
        "times new roman", 14, 'bold'), bg='white').place(x=50, y=100)
    Subject = StringVar()
    SubEntry = Entry(mainFrame, textvariable=Subject, font=(
        "times new roman", 14, 'bold'), bg='lightyellow')
    SubEntry.place(x=200, y=100)

    FileName = Label(mainFrame, text="Enter Filename", font=(
        "times new roman", 14, 'bold'), bg='white').place(x=50, y=150)
    name = StringVar()
    FileNameEntry = Entry(mainFrame, textvariable=name, font=(
        "times new roman", 14, 'bold'), bg='lightyellow')
    FileNameEntry.place(x=200, y=150)

    ############################################################### ENTRY FIELDS ###############################################################

    ################################################################# BUTTONS ##################################################################

    btn_generate = Button(mainFrame, text='QR Generate', font=("times new roman", 14, 'bold'),bg='#2196f3', fg='white', command=create_qr_code).place(x=10, y=250, width=140, height=30)
    btn_clear = Button(mainFrame, text='Clear', font=("times new roman", 14, 'bold'), bg='red',fg='white', command=clear_fields).place(x=210, y=250, width=100, height=30)
    btn_save = Button(mainFrame, text='Save', font=("times new roman", 14, 'bold'), bg='#607d8b',fg='white', command=save_qr_code).place(x=370, y=250, width=100, height=30)

    ################################################################# BUTTONS ##################################################################

    lbl_msg = Label(mainFrame, text='', font=("times new roman", 14), bg='white', fg='green')
    lbl_msg.place(x=0, y=320, relwidth=1)

    ################################################################# QR FIELD ##################################################################

    qr_Frame = Frame(root, bd=2, relief=RIDGE, bg='white')
    qr_Frame.place(x=600, y=150, width=250, height=380)
    qr_title = Label(qr_Frame, text="QR Code", font=("times new roman", 18), bg='#053246', fg='white').place(x=0, y=0, relwidth=1)

    qr_code = Label(qr_Frame, text='No QR\nAvailable', font=("times new roman", 15), bg='#053246', fg='white')
    qr_code.place(x=35, y=100, width=180, height=180)

    ################################################################# QR FIELD ##################################################################


root.mainloop()

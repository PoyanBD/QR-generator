import segno
import tkinter as tk

import tkinter as tk
from tkinter import simpledialog

def get_user_input():
    root = tk.Tk()
    root.withdraw()
    user_input = simpledialog.askstring("QR Generator", "Please enter your value:")
    
    return user_input

if __name__ == "__main__":
    valinput = get_user_input()
    filename = str(valinput) + ".png"

    qrcode = segno.make_qr(str(valinput))
    qrcode.save(filename, scale=7)


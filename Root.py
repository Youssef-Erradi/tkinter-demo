# encoding:utf-8
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
lbl = tk.Label(root)


def configuration():
    root.title("une fentre de teste")
    root.geometry("700x700")
    
def create_components():
    txt_nom = tk.Entry(root, text="default value")
    txt_nom.place(x=250, y=200)
    btn = tk.Button(root, text="Ahmed")
    btn["command"] = lambda button=btn : commancez(button["text"])
    btn.place(x=100, y=200)
    
def commancez(nom=None):
    messagebox.showinfo("titre", nom)
    lbl["text"] = nom
    lbl.place(x=250,y=250)
    # root.withdraw()
    # tk.Toplevel(root)
    

def setup_window():
    configuration()
    create_components()
    tk.mainloop()    

if __name__ == '__main__':
    setup_window()
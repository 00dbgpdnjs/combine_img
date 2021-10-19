# list vs combobox
import tkinter.ttk as ttk  # Can get the module as ttk
from tkinter import *  # Import tkinter moudule's everything(*)

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")  # width * height # Not * but x

values = [str(i) + "일" for i in range(1, 32)]  # day 1 ~ 31
# height: how many show at the same time / values: values of combobox
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("카드 결제일")

# readonly: can't enter only can select
readonly_combobox = ttk.Combobox(
    root, height=5, values=values, state="readonly")
readonly_combobox.current(0)  # Select the value of 0th idx as default
readonly_combobox.pack()


def btncmd():
    print(combobox.get())  # Print choosen value
    print(readonly_combobox.get())


btn = Button(root, text="선택", command=btncmd)
btn.pack()

root.mainloop()  # Not to be closed the window by using loop

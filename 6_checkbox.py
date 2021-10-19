# checkbox : Check pop-up

from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

# Save value to int in chkvar / 0: When releasing selection, 1: when checking
chkvar = IntVar()
# variable: variable(변화) after clicking the btn
chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar)
# chkbox.select() # Btn's choosen auto
# chkbox.deselct() # Release selection
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="일주일동안 보지 않기", variable=chkvar2)
chkbox2.pack()


def btncmd():
    print(chkvar.get())  # 0: When releasing selection, 1: when checking
    print(chkvar2.get())


btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()

# how much prgoressed -> Show to bar ex) when installing app
import time
import tkinter.ttk as ttk  # Can get the module as ttk
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

# The 2nd one means 100% / 3rd one when don't know when to finish. The opposite is "determinate"
progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
progressbar.start(10)  # Move by 10ms
progressbar.pack()


def btncmd():
    progressbar.stop()  # Stop running


btn = Button(root, text="중지", command=btncmd)
btn.pack()

# ----------------------------------------------

p_var2 = DoubleVar()  # why doubla : cuz reflecing a decimal place
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()


def btncmd2():
    for i in range(1, 101):  # (101) : 0 ~ 100
        time.sleep(0.01)  # Pause for 0.01s

        p_var2.set(i)  # Increase by i ; Set value of progress var
        # to reflect all movement based on the code above ; Whenever the for statement run, update UI
        progressbar2.update()
        # Useful when delivering messages according to percentages. ex) almost done, now we're doing...
        print(p_var2.get())


btn = Button(root, text="시작", command=btncmd2)
btn.pack()

root.mainloop()

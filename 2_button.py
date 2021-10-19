from tkinter import *

root = Tk()
root.title("Nado GUI")

# (where, ) / root var = main widnow, text attribute : Write
btn1 = Button(root, text="버튼1")
btn1.pack()  # Inclue but1 in root[main window] to see btn1

# pad : blank spaces / flexible base according to the text so not cut the letters.
btn2 = Button(root, padx=5, pady=10, text="버튼222222")
btn2.pack()

# rigit so can cut the letters
btn3 = Button(root, width=10, height=3, text="버튼3333333333")
btn3.pack()

btn4 = Button(root, fg="red", bg="yellow", text="버튼4")  # fg: font color
btn4.pack()

photo = PhotoImage(file="./img.png")
btn5 = Button(root, image=photo)
btn5.pack()


def btncmd():
    print("버튼이 클릭되었어요")


# Whenever clicking btn6, func of "command" will be run
btn6 = Button(root, text="동작하는 버튼", command=btncmd)
btn6.pack()

root.mainloop()

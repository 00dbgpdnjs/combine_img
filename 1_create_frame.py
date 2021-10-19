# GUI programming with tkinter 티킨터 which is GUI library  (Graphical User Interface)


from tkinter import *  # Import tkinter moudule's everything(*)

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")  # width * height # Not * but x
# root.geometry("640x480+100+300") # x-coordinate + y-coordinate  :  widnow position to be opened

root.resizable(False, False)  # (about width, hight) Can't resize

root.mainloop()  # Not to be closed the window by using loop

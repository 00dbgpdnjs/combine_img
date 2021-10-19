# listbox에 scrollbar 넣기 : 각각 서로를 mapping해줘야함.
# - listbox는 yscrollcommand = scrollbar.set, scrollbar는 scrollbar.config(command=listbox.yview)

from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

# It's comfy to manage by putting the scroll bar and the target widget [listbox] in one frame.
frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

# Refer to 5_listbox.py
# height=10 : Show by 10 data  / yscrollcommand : y (horizontal) scoroll / set : fasten[fix] scrolled scroller
listbox = Listbox(frame, selectmode="extended",
                  height=10, yscrollcommand=scrollbar.set)

for i in range(1, 32):
    listbox.insert(END, str(i) + "일")  # 1일, 2일, ... / END : in order [차곡차곡]
listbox.pack(side="left")

scrollbar.config(command=listbox.yview)

root.mainloop()

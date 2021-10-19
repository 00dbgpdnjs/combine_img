# listbox : a widget that manage list

from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

# selectmode="extended" : Can select several list / selectmode="single" : Can select only one / height=0 : Show all list / height=3 : Show 3 list. Press down key
listbox = Listbox(root, selectmode="extended", height=0)
listbox.insert(0, "사과")  # (idx,)
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")  # 1 2 3 이렇게 안하고 END 해도 끝에다[차례대로] 추가할 수 있음
listbox.insert(END, "포도")
listbox.pack()


def btncmd():
    # listbox.delete(END)  # Delete the last one
    # listbox.delete(0) # Delete the 1st item

    # size() : how many items in listbox
    #print("리스트에는", listbox.size(), "개가 있어요")

    #print("1번쨰부터 3번째까지의 항목 : ", listbox.get(0, 2))

    # curselection() : Print current selected items' idx
    print("선택된 항목 : ", listbox.curselection())


btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()

from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

# text widget like input tag
txt = Text(root, width=30, height=5)
txt.pack()
txt.insert(END, "글자를 입력하세요")  # insert: default value / (index[location],)

# text vs entry : Entry can enter only a line and can't run enter key. ex) login
e = Entry(root, width=30)
e.pack()
e.insert(0, "한 줄만 입력해요")


def btncmd():
    # 1.0 : from beginning (1 = 1st line, 0 = oth col[word]), END : to end  -> only in the txt case
    print(txt.get("1.0", END))
    print(e.get())  # Get and print e from beginning to end like the code above

    txt.delete("1.0", END)
    e.delete(0, END)


btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()

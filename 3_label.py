# label doesn't any run. just text or img

from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="./img.png")
label2 = Label(root, image=photo)
label2.pack()


def change():
    label1.config(text="또 만나요")

    # 버튼을 눌렀는데 photo2가 적용안된 이유: 돌아다니면서 쓰레기를 줍는 [불필요한 메모리 공간 해제] garbage collection 때문에 -> 전역변수로 선언해야 change 함수가 끝나도 photo2가 있어야 하니까 안 주음
    global photo2
    photo2 = PhotoImage(file="./img2.png")
    label2.config(image=photo2)


btn = Button(root, text="클릭", command=change)  # btn that change text of label1
btn.pack()

root.mainloop()

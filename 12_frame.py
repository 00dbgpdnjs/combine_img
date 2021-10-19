# to manage easily by putting wedgets(like buttons below) -> put buttons in a frame
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

# 레이블을 바로 루트에 집어넣을 수도 있고, 루트에 넣어진 윗젯에 넣을 수도 있음 아래 버튼 처럼
# default : side="like center"
Label(root, text="메뉴를 선택해 주세요").pack(side="top")

Button(root, text="주문하기").pack(side="bottom")

# relief : frame[border] shape / bd=1 : to represent line
frame_burger = Frame(root, relief="solid", bd=1)
# 1st arg: Place frame_burger on the left side. / 2nd one: frame_burger을 위아래(y) 좌우(x)로 채움 / 3rd : no empty space (of the right[next] widget) ; Exapnd to the right widget / If you don't understand, put in only one option and check
frame_burger.pack(side="left", fill="both", expand=True)

Button(frame_burger, text="햄버거").pack()
Button(frame_burger, text="치즈버거").pack()
Button(frame_burger, text="치킨버거").pack()

# LabelFrame : Frame having label[title]
frame_drink = LabelFrame(root, text="음료")
frame_drink.pack(side="right", fill="both", expand=True)
Button(frame_drink, text="콜라").pack()
Button(frame_drink, text="사이다").pack()

root.mainloop()

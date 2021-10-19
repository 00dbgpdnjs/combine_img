# eror pop-up

import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

# Train reservation system
# When clicking 알림 btn, you can see the msg


def info():
    # 1st arg is the title on top of the msgbox / The mark, blue !, is on msgbox cuz the msg is about into with showinfo()
    msgbox.showinfo("알림", "정상적으로 예매 완료되었습니다.")


def warn():
    msgbox.showwarning("경고", "해당 좌석은 매진되었습니다.")


def error():
    msgbox.showerror("에러", "결제 오류가 발생했습니다.")


def okcancel():
    # askokcancel() : Ask a user's opinion  ok or cancel
    msgbox.askokcancel("확인 / 취소", "해당 좌석은 유아동반석입니다. 예매하시겠습니까?")


def retrycancel():
    # askretrycancel() : Ask  retry or cancel
    response = msgbox.askretrycancel("재시도 / 취소", "일시적인 오류입니다. 다시 시도하시겠습니까?")
    if response == 1:
        print("재시도")
    elif response == 0:
        print("취소")


def yesno():
    msgbox.askyesno("예 / 아니오", "해당 좌석은 역방향입니다. 예매하시겠습니까?")


def yesnocancel():
    # 1st arg: When you don't want to write title alike the codes's 1st args above
    response = msgbox.askyesnocancel(
        title=None, message="예매 내역이 저장되지 않았습니다.\n저장 후 프로그램을 종료 하시겠습니까?")
    # If clicking yes, "True" will be printing. no - False, cancel - None
    print("응답 : ", response)
    # When processing, yes -1, no -2, otherwise
    if response == 1:
        print("예")
    elif response == 0:
        print("아니오")
    else:
        print("취소")


Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=error, text="에러").pack()
Button(root, command=okcancel, text="확인 취소").pack()
Button(root, command=retrycancel, text="재시도 취소").pack()
Button(root, command=yesno, text="예 아니오").pack()
Button(root, command=yesnocancel, text="예 아니오 취소").pack()

root.mainloop()

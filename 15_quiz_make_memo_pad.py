# Quiz) tkinter 를 이용한 메모장 프로그램을 만드시이ㅗ

# [GUI 조건]
# 1. 메모장 상단 :  title : 제목 없음 - Windows 메모장
# 2. 메뉴 : 파일, 편집, 서식, 보기, 도움말
# 3. 실세 메뉴 구현 : 파일 메뉴 내에서  열기, 저장, 끝내기 3개만 처리
# 3-1. 열기 클릭 시 : 이 파일과 같은 디렉토리에 저장된 mynote.txt 파일 내용 열어서 보여주기
# 3-2. 저장 클릭 시 : 이 파일과 같은 디렉토리에 mynote.txt 파일로 현재 내용 저장하기
# 3-3. 끝내기 클릭 시 : 프로그램 종료 ; x버튼 클릭하는 것과 같이
# 4. 프로그램 시작 시 메모장 본문이 비어 있어야 함
# 5. 실제 메모장 하단 처럼 status 바는 구현 안해도 됨
# 6. 프로그램 크기, 위치는 자유롭게 하되 크기 조정 가능해야 함
# 7. 본문 우측에 상하 스크롤 바 넣기

import os
from tkinter import *

root = Tk()
root.title("title : 제목 없음 - Windows 메모장")
root.geometry("640x480")

menu = Menu(root)

filename = "mynote.txt"


def open_file():
    if os.path.isfile(filename):
        with open(filename, "r", encoding="utf8") as file:  # (what, how-reading mode,)
            # 메모장에 텍스트가 있을 때 열기를 클릭 했을 때 기존 내용이 있으면 안되니까 / refer to 4_text_entry.py
            txt.delete("1.0", END)
            # insert : 읽어온 파일 내용을 본문(txt) 끝에 입력 / (where, what)
            txt.insert(END, file.read())


def save_file():
    with open(filename, "w", encoding="utf8") as file:
        # Write[save] all contents[("1.0", END)]
        file.write(txt.get("1.0", END))


menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command=open_file)
menu_file.add_command(label="저장", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="끝내기", command=root.quit)
menu.add_cascade(label="파일", menu=menu_file)

# 2번 구현
menu.add_cascade(label="편집")
menu.add_cascade(label="서식")
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")

# Body
# 프레임에 텍스트와 스크롤바를 넣지 않고 프레임이라 할 수 있는 루트에 둘을 넣음
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(side="left", fill="both", expand=True)  # both : x and y ; 위아래 좌우
scrollbar.config(command=txt.yview)

root.config(menu=menu)

root.mainloop()

# This file is a perfect program except to three options

import os
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import *
# cuz it's sub module which show a window to choose files
from tkinter import filedialog
from PIL import Image

root = Tk()
root.title("Nado GUI")


def add_file():
    # "files" will have choosen files / func : Open a window whick ask a user files / *.png : Show all files whose extension is png  as a combobox / initialdir : Open the path / r: row string ; 문법 해체 ; "r" is no need if changing "\"  to "/" or "\\"
    files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요", filetypes=(
        ("PNG 파일", "*.png"), ("모든 파일", "*.*")), initialdir=r"C:\Users\USER\Desktop\SW\project\python\combine_img")

    for file in files:
        # print(file)
        list_file.insert(END, file)


def del_file():
    # print(list_file.curselection()) # Print index of arr
    # If deleting 0 and 7, delete from the back with reversed() ; delete 0 after deleting 7 cuz if deleting 0 first, index is very likely to be changed.
    # reversed() : Refer to lst_reverse_and_zip.py
    for index in reversed(list_file.curselection()):
        list_file.delete(index)  # Delete among "list_file" based on "index"


def browse_dest_path():  # When clicking the "찾아보기" btn / 어디에 저장할지 폴더의 경로 선택하여 그 안에 파일로 저장
    # the func : Open a window which ask to choose a folder / Save the var of the choosen folder in folder_selected
    folder_selected = filedialog.askdirectory()
    if folder_selected is None:  # In case of clicking "취소" btn on the 폴더선택 window
        return  # Return an empty value
    # print(folder_selected)
    # (0, END) : from beginning to end / To delete previous value
    txt_dest_path.delete(0, END)
    # (where[which index], what) / insert():창에서  두번째 희색 박스 [저장 경로 박스 ; Entry]에 경로가 입력됨
    txt_dest_path.insert(0, folder_selected)


def merge_image():
    #print(list_file.get(0, END))
    images = [Image.open(x) for x in list_file.get(0, END)]
    # "images" >> [(width, height), ( , ), ( , ), ...]
    # This "x" obj has "size" -> size[0]:width, size[1]:height / images is arr

    #widths = [x.size[0] for x in images]
    #heights = [x.size[1] for x in images]

    # Use zip() instead of the two for statements above / Refer zip() to lst_reverse_and_zip.py
    widths, heights = zip(*(x.size for x in images))

    # Make a big stetchbook to merge images on it. Its width is the longest width among "widths" arr . Its height is adding all height.
    max_width, total_height = max(widths), sum(heights)
    #print("max width :", max_width)
    #print("total hight :", total_height)
    # Make a sketchbook / (,,bgcolor)
    result_img = Image.new("RGB", (max_width, total_height), (255, 255, 255))
    y_offset = 0  # location to merge under a img / y-coordinate of each image
    # !!!This for statement is key codes!!! Merge img / 2nd arg : coordinates to paste [붙이다]
    for idx, img in enumerate(images):
        result_img.paste(img, (0, y_offset))
        y_offset += img.size[1]

        progress = (idx + 1) / len(images) * 100  # Caculate percent
        p_var.set(progress)
        progress_bar.update()  # Update UI of progress_bar

    # path of the merged img : 1st arg + 2nd arg
    dest_path = os.path.join(txt_dest_path.get(), "nado_photo.jpg")
    result_img.save(dest_path)  # Save result_img at dest_path
    msgbox.showinfo("알림", "작업이 완료되었습니다.")


def start():  # When clicking "시작" btn, this func wil be run
    # Check value of three options, 가로넓이, 간격, 옵션,  to start this program
    # Get and print  the value of combobox whose label is "가로넓이"
    print("가로넓이 : ", cmb_width.get())
    print("간격 : ", cmb_space.get())
    print("포맷 : ", cmb_format.get())

    if list_file.size() == 0:  # When there is nothing in list_file, "시작" btn won't be run (due to the code, return) as showing a msgbox
        msgbox.showwarning("경고", "이미지 파일을 추가하세요")
        return  # Exit from this start() not to start this program

    if len(txt_dest_path.get()) == 0:  # len : length of the string, the gotten var
        msgbox.showwarning("경고", "저장 경로를 선택하세요")
        return

    merge_image()


# "파일추가"와 "선택삭제" 버튼을 file_frame 에 넣기
file_frame = Frame(root)
# fill: To occupy whole width cuz frame's size depend on btns's size
# pad : To make empty space between frames
file_frame.pack(fill="x", padx=5, pady=5)

btn_add_file = Button(file_frame, padx=5, pady=5,
                      width=12, text="파일추가", command=add_file)
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, padx=5, pady=5,
                      width=12, text="선택삭제", command=del_file)
btn_del_file.pack(side="right")


# Put listbox and scrollbar in one frame, list_frame
list_frame = Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)  # both : 위아래(y) 좌우(x)로 채움

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended",
                    height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)


# Put entry and btn in the frame, path_frame
path_frame = LabelFrame(root, text="저장경로")
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, padx=5, pady=5,
                   ipady=4)  # ipady : inner pad y

btn_dest_path = Button(path_frame, text="찾아보기",
                       width=10, command=browse_dest_path)
btn_dest_path.pack(side="right", padx=5, pady=5)


# Put options in the frame, frame_option
frame_option = LabelFrame(root, text="옵션")
frame_option.pack(padx=5, pady=5, ipady=5)

# 1) width setting option
lbl_width = Label(frame_option, text="가로넓이", width=8)
lbl_width.pack(side="left", padx=5, pady=5)

opt_width = ["원본유지", "1024", "800", "640"]
cmb_width = ttk.Combobox(frame_option, state="readonly",
                         values=opt_width, width=10)
cmb_width.current(0)
cmb_width.pack(side="left", padx=5, pady=5)

# 2) space between imgs setting option
lbl_space = Label(frame_option, text="간격", width=8)
lbl_space.pack(side="left", padx=5, pady=5)

opt_space = ["없음", "좁게", "보통", "넓게"]
cmb_space = ttk.Combobox(frame_option, state="readonly",
                         values=opt_space, width=10)
cmb_space.current(0)
cmb_space.pack(side="left", padx=5, pady=5)

# 3) file's format setting option
lbl_format = Label(frame_option, text="포맷", width=8)
lbl_format.pack(side="left", padx=5, pady=5)

opt_format = ["PNG", "JPG", "BMP"]
cmb_format = ttk.Combobox(
    frame_option, state="readonly", values=opt_format, width=10)
cmb_format.current(0)
cmb_format.pack(side="left", padx=5, pady=5)


# 진행 상황
frame_progess = LabelFrame(root, text="진행상황")
frame_progess.pack(fill="x", padx=5, pady=5, ipady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progess, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=5, pady=5)


# Put btn_close and btn_start in a frame
frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)

btn_close = Button(frame_run, padx=5, pady=5, text="닫기",
                   width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)

btn_start = Button(frame_run, padx=5, pady=5, text="시작",
                   width=12, command=start)
btn_start.pack(side="right", padx=5, pady=5)


root.resizable(False, False)
root.mainloop()

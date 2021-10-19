from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")


def create_new_file():
    print("새 파일을 만듭니다.")


menu = Menu(root)  # Start using menu to menu var
# 여러 탭을 만들더라도 이 코드는 한 줄이면 됨. "menu"라는 변수로 Menu()를 사용. 여러 탭 만들 시 이 변수에 만들 탭 개수 만큼 add_castate(label="tap name"). 한 탭에 리스트를 넣으려면 2번째 인자에 같은 변수로 넣으면 한 탭에 다 포함됨 / config 까지 해야 실제로 그려짐

# Create[Add] "File" tap[menu] like on top of VSC
# menu_file is list of a File menu[tap] among menu / teroff ??
menu_file = Menu(menu, tearoff=0)
# "command" will be run When clicking "New File"
menu_file.add_command(label="New File", command=create_new_file)
menu_file.add_command(label="New Window")
menu_file.add_separator()  # division line between menu's list
menu_file.add_command(label="Open File...")
menu_file.add_separator()
# "disable" makes "Save All" inactivation like when you save a file on VSC, Save All become inactivation state
menu_file.add_command(label="Save All", state="disable")
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)  # quit : End tkinter

# Put menu_file in menu var / "File" is name of menu
menu.add_cascade(label="File", menu=menu_file)
menu.add_cascade(label="Edit")

# Add "Language" tap[menu] to radiobutton
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="C++")
menu.add_cascade(label="Language", menu=menu_lang)

# Add View Menu to checkbutton
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="Show Minimap")
menu.add_cascade(label="View", menu=menu_view)

# same purpose to var.pack() but grammer is not same / pack() is used the case, 2~9)  to inclue menu var in root[main window]
root.config(menu=menu)
root.mainloop()

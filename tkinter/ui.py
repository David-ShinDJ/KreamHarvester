# import tkinter as tk
# from tkinter import ttk

# # 메인 창 생성
# window = tk.Tk()
# window.title("KREAM_즉구상품추출")

# # 유효기간 정보 (라벨)
# valid_date_label = ttk.Label(window, text="유효기간: 2025-02-16 (D-187)")
# valid_date_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# # 마진율 정보 (라벨)
# margin_label = ttk.Label(window, text="(참고) 마진률 = (보판가-즉구가)/즉구가")
# margin_label.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

# # 로그인 정보 (라벨, 입력 필드, 버튼)
# login_label = ttk.Label(window, text="1. 로그인")
# login_label.grid(row=2, column=0, padx=10, pady=10)

# id_label = ttk.Label(window, text="아이디(ID)")
# id_label.grid(row=3, column=0, padx=10, pady=10)

# id_entry = ttk.Entry(window)
# id_entry.grid(row=3, column=1, padx=10, pady=10)

# pw_label = ttk.Label(window, text="비밀번호(PASS)")
# pw_label.grid(row=4, column=0, padx=10, pady=10)

# pw_entry = ttk.Entry(window, show="*")  # 비밀번호 가리기
# pw_entry.grid(row=4, column=1, padx=10, pady=10)

# login_button = ttk.Button(window, text="로그인")
# login_button.grid(row=5, column=1, padx=10, pady=10)

# # ... (나머지 UI 요소 추가) ...

# window.mainloop()

import tkinter as tk

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.entrythingy = tk.Entry()
        self.entrythingy.pack()

        # Create the application variable.
        self.contents = tk.StringVar()
        # Set it to some value.
        self.contents.set("this is a variable")
        # Tell the entry widget to watch this variable.
        self.entrythingy["textvariable"] = self.contents

        # Define a callback for when the user hits return.
        # It prints the current value of the variable.
        self.entrythingy.bind('<Key-Return>',
                             self.print_contents)

    def print_contents(self, event):
        print("Hi. The current entry content is:",
              self.contents.get())

root = tk.Tk()
myapp = App(root)
myapp.mainloop()


import tkinter as tk

def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, str(current) + str(number))

def button_clear():
    display.delete(0, tk.END)

def button_equal():
    try:
        result = str(eval(display.get()))
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")

# 메인 창 생성
window = tk.Tk()
window.title("간단한 계산기")

# 디스플레이
display = tk.Entry(window, width=35, borderwidth=5)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# 버튼 생성
button_list = [
    'C', ' ', ' ', '/',
    '7', '8', '9', '*',
    '4', '5', '6', '-',
    '1', '2', '3', '+',
    '0', '.', '='
]
row_num = 1
col_num = 0
for button_text in button_list:
    button = tk.Button(window, text=button_text, width=9, height=4,
                        command=lambda text=button_text: button_click(text) if text != '=' else button_equal() if text == '=' else button_clear())
    button.grid(row=row_num, column=col_num, padx=5, pady=5)
    col_num += 1
    if col_num > 3:
        col_num = 0
        row_num += 1

# 메인 루프 실행
window.mainloop()
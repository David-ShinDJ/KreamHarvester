import tkinter as tk
from tkinter import ttk
# 메인 창 생성
window = tk.Tk()
window.title("KreamHarvester")

## 로그인구현
def login():
    value = id_entry.get(), pw_entry.get()
    print(value)

login_label = ttk.Label(window, text="로그인구현")
login_label.grid(row=0, column=0, padx=10, pady=10)

id_entry = ttk.Entry(window)
id_entry.grid(row=0, column=1, padx=10, pady=10)

pw_entry = ttk.Entry(window, show="*")
pw_entry.grid(row=0, column=2, padx=10, pady=10)

login_button = ttk.Button(window, text="로그인", command=login)
login_button.grid(row=0, column=3, padx=10, pady=10)

## 검색조건구현
serach_label = ttk.Label(window, text="검색조건")
serach_label.grid(row=1, column=0, padx=10, pady=10)

category_combobox = ttk.Combobox(window, values=["카테고리1", "카테고리2", "카테고리3"])
category_combobox.grid(row=1, column=1, padx=10, pady=10)

page_spinbox = ttk.Spinbox(window, from_=1, to=100)
page_spinbox.grid(row=1, column=2, padx=10, pady=10)

notebook_box = ttk.Notebook(window)
notebook_box.grid(row=1, column=3, padx=10, pady=10)

def serach():
    value = category_combobox.get()
    print(value)

serach_button = ttk.Button(window, text="검색", command=serach)
serach_button.grid(row=1, column=3, padx=10, pady=10)

window.mainloop()
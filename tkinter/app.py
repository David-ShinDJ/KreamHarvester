import tkinter as tk
from tkinter import ttk
import time
import threading

class App:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("KreamHarvester")
        
        # 메인 프레임 생성
        self.main_frame = ttk.Frame(self.window)
        self.main_frame.pack(expand=True, fill='both')
        self.window.geometry("800x600")  # 초기 창 크기 설정
        self.window.resizable(True, True)  # 창 크기 조절 가능
        
        # 왼쪽 프레임 (노트북용)
        self.left_frame = ttk.Frame(self.main_frame)
        self.left_frame.pack(side='left', expand=True, fill='both', padx=5, pady=5)
        # 스타일 설정
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TButton", font=('Arial', 12), padding=6, relief="flat",
                        background='#0077FF', foreground='white')  # Kream 스타일 버튼
        style.map("TButton",
              foreground=[('pressed', 'white'), ('active', 'white')],
              background=[('pressed', '!disabled', '#0056b3'), 
                          ('active', '#0066CC')])  # 버튼 hover 효과
        style.configure("TLabel", font=('Arial', 11))
        style.configure("TEntry", font=('Arial', 11))
        style.configure("TFrame", background='white')
        style.configure("TNotebook", tabposition='wn')  # 탭 위치 변경
        style.configure("TNotebook.Tab", font=('Arial', 11))
        style.configure("Horizontal.TProgressbar",
                    background='#0077FF',  # Kream 스타일 프로그레스 바
                    troughcolor='lightgray',
                    thickness=20)

        # 노트북 생성
        self.notebook = ttk.Notebook(self.left_frame)
        self.notebook.pack(expand=True, fill='both')
        
        # 페이지 1: 기본 모드
        self.page1 = ttk.Frame(self.notebook)
        self.notebook.add(self.page1, text='기본 모드')
        self.setup_page1()
        
        # 페이지 2: 고급 모드
        self.page2 = ttk.Frame(self.notebook)
        self.notebook.add(self.page2, text='고급 모드')
        self.setup_page2()
        
        # 오른쪽 프레임 (결과 요약용)
        self.right_frame = ttk.LabelFrame(self.main_frame, text="결과 요약")
        self.right_frame.pack(side='right', fill='both', padx=5, pady=5)
        
        # 결과 요약 텍스트 영역
        self.setup_result_area()

    def setup_page1(self):
        # 스타일 설정
        style = ttk.Style()
        style.theme_use('clam')  # 테마 변경
        style.configure("TButton", font=('Arial', 12), padding=10)
        style.configure("TLabel", font=('Arial', 12))
        style.configure("TEntry", font=('Arial', 12))
        style.configure("Horizontal.TProgressbar", 
                    background='green',  # 프로그레스 바 색상 변경
                    troughcolor='lightgray',
                    thickness=20)

        """기본 모드 페이지 설정"""
        # 입력 프레임
        input_frame = ttk.Frame(self.page1)
        input_frame.pack(padx=10, pady=10)
        
        # 로그인 섹션
        login_label = ttk.Label(input_frame, text="로그인")
        login_label.grid(row=0, column=0, padx=5, pady=5)
        
        self.id_entry = ttk.Entry(input_frame)
        self.id_entry.grid(row=0, column=1, padx=5, pady=5)
        
        self.pw_entry = ttk.Entry(input_frame, show="*")
        self.pw_entry.grid(row=0, column=2, padx=5, pady=5)
        
        # 검색 섹션
        search_label = ttk.Label(input_frame, text="키워드")
        search_label.grid(row=1, column=0, padx=5, pady=5)
        
        self.keyword_entry = ttk.Entry(input_frame)
        self.keyword_entry.grid(row=1, column=1, padx=5, pady=5)
        
        count_label = ttk.Label(input_frame, text="수집 개수")
        count_label.grid(row=1, column=2, padx=5, pady=5)
        
        self.count_spinbox = ttk.Spinbox(input_frame, from_=1, to=100)
        self.count_spinbox.set(1)
        self.count_spinbox.grid(row=1, column=3, padx=5, pady=5)
        
        # 진행 상태 표시
        progress_frame = ttk.Frame(self.page1)
        progress_frame.pack(padx=10, pady=5, fill='x')
        
        self.progress_label = ttk.Label(progress_frame, text="진행 상태: 0%")
        self.progress_label.pack()
        
        # 프로그레스바 스타일 설정
        style = ttk.Style()
        style.configure("Horizontal.TProgressbar", 
                    background='blue',
                    troughcolor='lightgray',
                    thickness=20)
        
        self.progress_bar = ttk.Progressbar(
            progress_frame, 
            orient='horizontal',
            length=300, 
            mode='determinate',
            style="Horizontal.TProgressbar"
        )
        self.progress_bar.pack(pady=5)
        
        # 실행 버튼
        self.run_button = ttk.Button(self.page1, text="실행", command=self.run_script)
        self.run_button.pack(pady=10)

    def setup_page2(self):
        """고급 모드 페이지 설정"""
        # 스타일 설정
        style = ttk.Style()
        style.theme_use('clam')  # 테마 변경
        style.configure("TButton", font=('Arial', 12), padding=10)
        style.configure("TLabel", font=('Arial', 12))
        style.configure("TEntry", font=('Arial', 12))
        # 입력 프레임
        input_frame = ttk.Frame(self.page2)
        input_frame.pack(padx=10, pady=10)
        
        # 로그인 섹션 (고급 모드)
        login_label = ttk.Label(input_frame, text="로그인")
        login_label.grid(row=0, column=0, padx=5, pady=5)
        
        self.id_entry_adv = ttk.Entry(input_frame)
        self.id_entry_adv.grid(row=0, column=1, padx=5, pady=5)
        
        self.pw_entry_adv = ttk.Entry(input_frame, show="*")
        self.pw_entry_adv.grid(row=0, column=2, padx=5, pady=5)
        
        # 검색 섹션 (고급 모드)
        search_label = ttk.Label(input_frame, text="키워드")
        search_label.grid(row=1, column=0, padx=5, pady=5)
        
        self.keyword_entry_adv = ttk.Entry(input_frame)
        self.keyword_entry_adv.grid(row=1, column=1, padx=5, pady=5)

        category_label = ttk.Label(input_frame, text="카테고리")
        category_label.grid(row=1, column=2, padx=5, pady=5)

        self.category_combobox = ttk.Combobox(input_frame, values=["카테고리1", "카테고리2", "카테고리3"])
        self.category_combobox.current(0)
        self.category_combobox.grid(row=1, column=3, padx=5, pady=5)
        
        count_label = ttk.Label(input_frame, text="수집 개수")
        count_label.grid(row=1, column=4, padx=5, pady=5)
        
        self.count_spinbox_adv = ttk.Spinbox(input_frame, from_=1, to=100)
        self.count_spinbox_adv.set(1)
        self.count_spinbox_adv.grid(row=1, column=5, padx=5, pady=5)
        
        # 추가 옵션 섹션
        options_frame = ttk.LabelFrame(self.page2, text="추가 옵션")
        options_frame.pack(padx=10, pady=5, fill='x')
        
        self.auto_login_var = tk.BooleanVar()
        auto_login_check = ttk.Checkbutton(options_frame, text="자동 로그인", variable=self.auto_login_var)
        auto_login_check.pack(side='left', padx=5)
        
        self.save_data_var = tk.BooleanVar()
        save_data_check = ttk.Checkbutton(options_frame, text="데이터 저장", variable=self.save_data_var)
        save_data_check.pack(side='left', padx=5)
        
        # 진행 상태 표시 (고급 모드)
        progress_frame = ttk.Frame(self.page2)
        progress_frame.pack(padx=10, pady=5, fill='x')
        
        self.progress_label_adv = ttk.Label(progress_frame, text="진행 상태: 0%")
        self.progress_label_adv.pack()
        
        self.progress_bar_adv = ttk.Progressbar(
            progress_frame, 
            orient='horizontal',
            length=300, 
            mode='determinate',
            style="Horizontal.TProgressbar"
        )
        self.progress_bar_adv.pack(pady=5)
        
        # 실행 버튼 (고급 모드)
        self.run_button_adv = ttk.Button(self.page2, text="실행", command=self.run_script_advanced)
        self.run_button_adv.pack(pady=10)

    def setup_result_area(self):
        """결과 요약 영역 설정"""
         # 폰트 변경
        # 텍스트 위젯과 스크롤바 프레임
        text_frame = ttk.Frame(self.right_frame)
        text_frame.pack(expand=True, fill='both', padx=5, pady=5)
        
        # 스크롤바 생성
        scrollbar = ttk.Scrollbar(text_frame)
        scrollbar.pack(side='right', fill='y')
        
        # 텍스트 위젯 생성
        self.result_text = tk.Text(
            text_frame,
            wrap=tk.WORD,
            width=40,  # 텍스트 영역 너비
            height=20,  # 텍스트 영역 높이
            yscrollcommand=scrollbar.set
        )
        self.result_text.pack(side='left', expand=True, fill='both')
        self.result_text.config(font=('Arial', 10)) 
        
        # 스크롤바 연결
        scrollbar.config(command=self.result_text.yview)
        
        # 초기 텍스트 설정
        self.result_text.insert('1.0', "수집 결과가 여기에 표시됩니다.\n")
        self.result_text.config(state='disabled')  # 읽기 전용으로 설정

    def add_result(self, text):
        """결과 텍스트 추가"""
        self.result_text.config(state='normal')  # 쓰기 가능하도록 변경
        self.result_text.insert('end', f"{text}\n")
        self.result_text.see('end')  # 스크롤을 맨 아래로
        self.result_text.config(state='disabled')  # 다시 읽기 전용으로 설정

    def update_progress(self, current, total, advanced=False):
        """진행률 업데이트"""
        progress = (current / total) * 100
        if advanced:
            self.progress_bar_adv['value'] = progress
            self.progress_label_adv['text'] = f"진행 상태: {progress:.1f}%"
        else:
            self.progress_bar['value'] = progress
            self.progress_label['text'] = f"진행 상태: {progress:.1f}%"
        self.window.update_idletasks()

    def run_script(self):
        """기본 모드 실행"""
        try:
            # 기본 모드 입력값 처리
            login_info = {
                'id': self.id_entry.get(),
                'password': self.pw_entry.get()
            }
            
            count_value = self.count_spinbox.get().strip()
            if not count_value.isdigit():
                self.progress_label['text'] = "수집 개수는 숫자여야 합니다."
                return
            
            search_info = {
                'keyword': self.keyword_entry.get(),
                'count': int(count_value)
            }
            
            # 프로그레스바 초기화
            self.progress_bar['value'] = 0
            self.progress_label['text'] = "진행 상태: 0%"
            
            # 수집 작업을 별도 스레드에서 실행
            thread = threading.Thread(
                target=self.run_collection,
                args=(search_info, False)
            )
            thread.daemon = True
            thread.start()
            
        except Exception as e:
            self.progress_label['text'] = f"오류 발생: {str(e)}"

    def run_script_advanced(self):
        """고급 모드 실행"""
        try:
            # 고급 모드 입력값 처리
            login_info = {
                'id': self.id_entry_adv.get(),
                'password': self.pw_entry_adv.get(),
                'auto_login': self.auto_login_var.get()
            }
            
            count_value = self.count_spinbox_adv.get().strip()
            if not count_value.isdigit():
                self.progress_label_adv['text'] = "수집 개수는 숫자여야 합니다."
                return
            
            search_info = {
                'keyword': self.keyword_entry_adv.get(),
                'category': self.category_combobox.get(),
                'count': int(count_value),
                'save_data': self.save_data_var.get()
            }
            
            # 프로그레스바 초기화
            self.progress_bar_adv['value'] = 0
            self.progress_label_adv['text'] = "진행 상태: 0%"
            
            # 수집 작업을 별도 스레드에서 실행
            thread = threading.Thread(
                target=self.run_collection,
                args=(search_info, True)
            )
            thread.daemon = True
            thread.start()
            
        except Exception as e:
            self.progress_label_adv['text'] = f"오류 발생: {str(e)}"

    def run_collection(self, search_info, advanced=False):
        """실제 수집 작업을 수행하는 메서드"""
        total_items = search_info['count']
        
        # 수집 시작 메시지
        self.window.after(0, self.add_result, 
                         f"수집 시작: 키워드 '{search_info.get('keyword')}', 목표 {total_items}개")
        
        for i in range(total_items):
            time.sleep(0.5)
            self.window.after(0, self.update_progress, i + 1, total_items, advanced)
            
            # 예시: 각 항목 수집 결과 추가
            self.window.after(0, self.add_result, 
                             f"항목 {i+1} 수집 완료: 예시 상품명")
        
        # 완료 메시지
        completion_message = "수집 완료!"
        if advanced:
            self.window.after(0, lambda: setattr(self.progress_label_adv, 'text', completion_message))
        else:
            self.window.after(0, lambda: setattr(self.progress_label, 'text', completion_message))
        
        self.window.after(0, self.add_result, 
                         f"\n총 {total_items}개 항목 수집 완료\n{'='*40}")

    def run(self):
        self.window.mainloop()
    
if __name__ == "__main__":
    app = App()
    app.run()

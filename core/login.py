from utils import *
from seleniumbase import SB
from utils.pause import pause_while

class Login:
    def __init__(self, email, password, sb):
        self.email = email
        self.password = password
        self.sb = sb  # seleniumbase 인스턴스 저장
    
    def perform_login(self):
        try:
            self.sb.open("https://kream.co.kr/")
            self.sb.click('a[href="/login"]')
            self.sb.type('input[type="email"]', self.email)
            self.sb.type('input[type="password"]', self.password)
            self.sb.click('button[type="submit"]')
        
        except Exception as e:
            print(f"로그인 실패: {e}")
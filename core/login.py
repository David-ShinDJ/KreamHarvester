
from seleniumbase import SB
from src.utils.pause import pause_while

class Login:
    def __init__(self, sb):
        self.sb = sb  # seleniumbase 인스턴스 저장
    
    def perform_login(self, email, password):
        try:
            self.sb.open("https://kream.co.kr/")
            self.sb.click('a[href="/login"]')
            self.sb.type('input[type="email"]', email)
            self.sb.type('input[type="password"]', password)
            self.sb.click('button[type="submit"]')
        
        except Exception as e:
            print(f"로그인 실패: {e}")
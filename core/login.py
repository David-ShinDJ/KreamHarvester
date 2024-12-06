from utils import *
from seleniumbase import SB



class Login:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def perform_login(self):
        with SB() as sb:
            sb.open("https://kream.co.kr/")
            sb.click('a:contains("로그인")')
            sb.type('input[type="email"]', self.email)
            sb.type('input[type="password"]', self.password)
            sb.click('button[type="submit"]')
            sb.wait_for_element('a:contains("로그아웃")')

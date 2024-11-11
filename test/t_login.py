from seleniumbase import BaseCase
from parameterized import parameterized

test_email = "ehdwnsqkqhek@naver.com"
test_password = "Tls1169511!"
class TestLogin(BaseCase):
    @parameterized.expand([(test_email, test_password)])
    def test_perform_login(self, email: str, password: str):
        try:
            self.open("https://kream.co.kr/")
            self.click('a:contains("로그인")')
            self.type('input[type="email"]', email)
            self.type('input[type="password"]', password)
            self.click('button[type="submit"]')
            self.wait_for_element('a:contains("로그아웃")')
            print("로그인 성공!")
        except Exception as e:
            print(f"로그인 실패: {e}")
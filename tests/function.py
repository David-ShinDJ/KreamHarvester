## 크롤링에서 자주사용하는 SeleniumBase 함수선언하기
from seleniumbase import BaseCase
from parameterized import parameterized
import pytest

def pause_while(bool=True):
    """
    auto_mode가 False일 때만 사용자 입력을 기다립니다.
    True일 경우 자동으로 계속 진행됩니다.
    """
    if bool:
        while True:
            var = input("sb 중지를 멈추려면 0 입력하세요 : ")
            if var == "0":
                break
    else:
        return


class TestFunction(BaseCase):
    def setUp(self):
        super().setUp()
        # 추가 초기화가 필요한 경우 여기에 작성
    def tearDown(self):
        super().tearDown()

    # @parameterized.expand([
    #     # 성공 케이스
    #     ("https://kream.co.kr/login", "email", "ehdwnsqkqhek@naver.com", "password", "Tls1169511!", "btn.full.solid", True, None),
    #     # 실패 케이스 - 잘못된 비밀번호
    #     ("https://kream.co.kr/login", "email", "wrong@email.com", "password", "123432131414", "btn.full.solid", False, "이메일 또는 비밀번호를 확인해주세요."),
    #     # 빈 필드 케이스
    #     ("https://kream.co.kr/login", "email", "", "password", "", "btn.full.solid", False, "이메일을 입력해주세요."),
    # ])
    # def test_open_login(self, url, input_type, input_value, input_type2, input_value2, 
    #                    button_class_name, expected_success, expected_error):
    #     """열기 및 로그인 테스트"""
    #     try:
    #         self.open(url)
    #         self.type(f'input[type="{input_type}"]', input_value)
    #         self.type(f'input[type="{input_type2}"]', input_value2)
    #         self.click(f'button.{button_class_name}')
            
    #         if expected_success:
    #             # 로그인 성공 케이스
    #             self.assert_element_present('a[href="/"].top_link')
    #         else:
    #             # 로그인 실패 케이스
    #             # 에러 메시지가 표시되는 요소의 선택자를 찾아서 수정해야 합니다
    #             # 예시: 'p.error_message' 또는 'div.alert' 등
    #             self.assert_url("https://kream.co.kr/login")
                
    #     except Exception as e:
    #         print(f"로그인 테스트 실패: {str(e)}")

    # @parameterized.expand([
    #     ("https://kream.co.kr/search", "카테고리", "바람막이"),
    #     ("https://kream.co.kr/search", "혜택/할인", "장갑"),
    #     ("https://kream.co.kr/search", "가격대", "러그")
    # ])
    # def test_open_set_filter(self, url, click_modal_text, category_text):
    #     """필터 기능 테스트"""
    #     try:
    #         self.open(url)
    #         self.click(f'span.title:contains("{click_modal_text}")')
    #         self.wait_for_element(f'h2.title.search-filter-title')
    #         """필터 모달 초기화"""
    #         self.click('div.shop-filter-sections.gender.expanded span.collapse-icon')
    #         self.click('div.shop-filter-sections.benefits.expanded span.collapse-icon')
    #         self.click('div.shop-filter-sections button:contains("더보기")')
    #         self.click(f'div.layer_container span:contains({category_text})')

    #     except Exception as e:
    #         print(f"필터 테스트 실패: {e}")
    
    # @parameterized.expand([
    #     ("https://kream.co.kr", "나이키", 0),
    #     ("https://kream.co.kr", "루이비통", 2),
    #     ("https://kream.co.kr", "숏패딩", 5)
    # ])
    # def test_search_click_product(self, url, keyword, number_of_product):
    #     """ 제품 검색 및 클릭 """
    #     try:
    #         self.open(url)
    #         self.click("button.btn_search")
    #         ## 검색 및 Press Enter
    #         self.type('input[type="text"]', keyword + "\n")
    #         self.click(f'div.search_result_list div.search_result_item.product[data-result-index="{number_of_product}"]')
    #     except Exception as e:
    #         print(f"제품 검색 테스트 실패: {e}")

    @parameterized.expand([
        ("https://kream.co.kr/search?keyword=지갑", 10),
        ("https://kream.co.kr/search?keyword=에어포스", 30),    
        ("https://kream.co.kr/search?keyword=패딩", 50),

    ])# 1초 대기 후 재시도

    ## TODO: index 50이상시 스크롤 기능 , 페이지가 완전 로드되기전에 back 한경우 data; 이상한페이지로드됨, 네트워크속도,오류발생시 프로그램이 멈춤
    ## TODO: self.wait 페이지로드시 필요한 함수, self.sleep 스크립트작업을 아예끄는방식 모든 작업이 끝날떄 sleepp 사용해야함
    def test_extract_products(self, url, number_of_products):
        retry_count = 0
        max_retries = 3

        while retry_count < max_retries:
            try:
                self.open(url)
                for i in range(0, number_of_products):
                    self.wait(1)
                    if self.is_element_present(f'div.search_result_list div.search_result_item.product[data-result-index="{i}"]'):
                        self.click(f'div.search_result_list div.search_result_item.product[data-result-index="{i}"]')
                        self.wait(1)
                        self.go_back()
                    else:
                        self.scroll_to(f'div.search_result_list div.search_result_item.product[data-result-index="{i+1}"]')
                        if self.is_element_present(f'div.search_result_list div.search_result_item.product[data-result-index="{i}"]'):
                            self.click(f'div.search_result_list div.search_result_item.product[data-result-index="{i}"]')
                            self.wait(1)
                            self.go_back()
                    self.wait(1)
                
                return 
            except Exception as e:
                print(f"제품 추출 테스트 실패: {e}")
                retry_count += 1
                self.sleep(1)
            finally:
                print(f'{retry_count}회 실행중')
    ## TODO: Product Info Write 하기
    @parameterized.expand([
        ("https://kream.co.kr/search?keyword=지갑", 10),
        ("https://kream.co.kr/search?keyword=에어포스", 30),    
        ("https://kream.co.kr/search?keyword=패딩", 50),

    ])#
    def test_write_product_excel(self):
        pass


if __name__ == "__main__":
    pytest.main(['tests/function.py', '-v', '-s']) # 테스트 파일 경로 지정
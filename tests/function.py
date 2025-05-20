## 유닛함수및 테스트케이스 작성 
import pytest
from seleniumbase import BaseCase
from src.models.thumb import Thumbnail
from parameterized import parameterized
## FIXME: 이슈모음
## 1. typing 인식안돼는 이슈 존재
        # self.click("button.btn_search.header-search-button.search-button-margin")
         # ## typing 인식안돼는 이슈 존재
        # self.type('input[type="text"]', "조던 + \n")
## 3. data; 페이지가 로드되는경우 잘못된요소를 클릭하거나 이동하면발생함 없는요소를 클릭하는 함수실행시 발생함
    # self.wait 페이지로드시 사용하여 방지 , self.sleep는 스크립트작업을 아예끄는방식으로 모든 작업이 끝날떄 사용필요
## 4. 단어의 띄어쓰기있는경우 
    #self.click('li.sorting_item p:contains("%s")' % test_sorting) %s 문법사용해야함
    ## 인덱스 늘어나는 범위 0~51 52~101 102~151 152~201 202~251 252~301
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
    #     ("https://kream.co.kr/login", "email", ""~, "password", "", "btn.full.solid", False, "이메일을 입력해주세요."),
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
        # (Filter(category1="신발", category2="스니커즈", 
        #         keyword="조던", sort_by="남성 인기순", min_margin=10,
        #         exclude_storage=True, exclude_release_above=False, 
        #         exclude_no_release=False, min_total_sales=5, min_period_sales=5,
        #           min_immediate_price=200000, max_immediate_price=1000000, size_options="260,265,270")),
    #     (Filter(category1="아우터", category2="바람막이", 
    #             keyword="바람막이", sort_by="인기순", min_margin=20,
    #             exclude_storage=False, exclude_release_above=False, 
    #             exclude_no_release=True, min_total_sales=2, min_period_sales=3,
    #               min_immediate_price=100000, max_immediate_price=1000000, size_options="모든사이즈")),
    #     (Filter(category1="패션잡화", category2="팔찌", 
    #             keyword="팔찌", sort_by="여성 인기순", min_margin=30,
    #             exclude_storage=True, exclude_release_above=True, 
    #             exclude_no_release=True, min_total_sales=3, min_period_sales=2,
    #               min_immediate_price=50000, max_immediate_price=1000000, size_options="사이즈옵션없음")),
        
    # ])

    # def test_set_filter(self, filter: Filter):
    #     """필터 기능 테스트"""
    #     try:
    #         self.open(f"https://kream.co.kr/search?keyword={filter.keyword}")
    #         self.click(f'span.title:contains("카테고리")')
    #         self.wait_for_element(f'h2.title.search-filter-title')
    #         """필터 모달 초기화"""
    #         self.click('div.shop-filter-sections.gender.expanded span.collapse-icon')
    #         self.click('div.shop-filter-sections.benefits.expanded span.collapse-icon')
    #         self.click('div.shop-filter-sections button:contains("더보기")')
    #         self.click(f'div.layer_container span:contains({filter.category2})')
    #         self.click('a.btn.full.solid')
    #         self.click('div.content-container button.sorting_title')
    #         self.click(f'li.sorting_item p:contains("{filter.sort_by}")')
            
    #     except Exception as e:
    #         print(f"필터 테스트 실패: {e}")
    
    # @parameterized.expand([
    #     ("https://kream.co.kr/products/84450", "사이즈옵션없음"),
    #     ("https://kream.co.kr/products/235976",["S", "M", "L", "XL", "XXL"]),
    #     ("https://kream.co.kr/products/430299", ["220", "225", "230", "235", "240", "245", "250", "255", "260", "265", "270", "275", "280", "285", "290", "295", "300", "305", "310", "315", "320", "325"]),
    #     ("https://kream.co.kr/products/57394", ["26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38"]),
    #     ("https://kream.co.kr/products/147583", ["S-M", "M-L", "L-XL"]),
    # ])#
    # def test_click_size(self, url, size_options):
    #     try:
    #         ## 로그인 진행
    #         self.open("https://kream.co.kr/login")
    #         self.type('input[type="email"]', "ehdwnsqkqhek@naver.com")
    #         self.type('input[type="password"]', "Tls1169511!")
    #         self.click('button[type="submit"]')
    #         self.wait(1)
    #         self.open(url)
    #         if size_options == "사이즈옵션없음":
    #             return
    #         else:
    #             self.click('span.title-txt:contains("모든 사이즈")')
    #             if self.is_element_present('div.layout-grid-horizontal-equal.select_list.grid_list.grid_3'):
    #                 size_option = self.get_text('div.layout-grid-horizontal-equal.select_list.grid_list.grid_3')
    #                 option_list = size_option.split("\n")
    #                 common_sizes = [size for size in size_options if size in option_list]
    #                 for size in common_sizes:
    #                     self.click(f'div.text_body.option1 p.text-lookup:contains("{size}")')
    #                     self.click(f'span.title-txt:contains("{size}")')
    #             self.go_back()
    #     except Exception as e:
    #         print(f"테스트 실행 중 오류 발생: {str(e)}")
    # @parameterized.expand([49, 51, 99, 101, 151, 199, 201])
    # def test_scroll_down(self, index: int):
    #     quotient = index // 50 + 1
    #     self.open("https://kream.co.kr/search")
    #     for i in range(quotient):
    #         self.scroll_to_bottom()
    #         self.wait(1)
    #         self.slow_scroll_to_element(f'div[data-result-index="{i*50}"]')
    #         if i == quotient - 1:
    #             self.scroll_to_element(f'div[data-result-index="{index}"]')
    #     print(f"index: {index}, quotient: {quotient}")
    # @parameterized.expand([1, 49, 51, 99, 101, 199, 201])
    # def test_click_product_index(self, index: int):
    #     quotient = index // 50 + 1
    #     try:
    #         self.open("https://kream.co.kr/search")
    #         for i in range(quotient):
    #             self.scroll_to_bottom()
    #             self.wait(1)
    #             self.slow_scroll_to_element(f'div[data-result-index="{i*50}"]')
    #             if i == quotient - 1:
    #                 self.scroll_to_element(f'div[data-result-index="{index}"]')
    #         self.click(f'div[data-result-index="{index}"].search_result_item.product')
    #         pause()
    #     except Exception as e:
    #         print(f"제품 클릭실패: {e}")
    @parameterized.expand([
        1
    ])
    def test_extract_thumbnail_info(self, index: int,):
        """ 제품 검색 및 클릭 """
        try:
            self.open("https://kream.co.kr/search")
            thumbnail_info = Thumbnail(index=index)
            text = self.get_text(f'div[data-result-index="{index}"]')
            text_list = text.split("\n")# 디버깅용 출력
            thumbnail_info.trade_volume = text_list[0].replace("거래 ", "")  # "거래 1.3만" -> "1.3만"
            thumbnail_info.brand = text_list[1]  # "Asics"
            thumbnail_info.name = text_list[3]   # "아식스 젤 소노마 15-50 블랙"
            thumbnail_info.lowest_immediate_buy_price = text_list[5].replace("원", "").replace(",", "")  # "145,000원" -> "145000"
            thumbnail_info.likes = text_list[7]  # "3.2만"
            thumbnail_info.reviews = text_list[8]  # "236"
        except Exception as e:
            print(f"제품 검색 테스트 실패: {e}")
        finally:
            print(f"포인터 정보: {thumbnail_info}")

## product 추출 데이터
                #  name: str,                    # 제품_이름
                #  url: str,                      # 제품_URL
                #  product_id: str,               # 제품_id
                #  category: str,                 # 제품_카테고리
                #  brand: str,                    # 브랜드
                #  model_number: str,             # 제품_품번
                #  immediate_buy_price: int,      # 즉시구매가격
                #  storage_sell_price: int,       # 보관판매가격
                #  immediate_sell_price: int,     # 즉시판매가격
                #  total_sales: int,              # 총판매량
                #  storage_latest_date: str,      # 보판_최근체결날짜
                #  storage_latest_price: int,     # 보판_최근체결금액
                #  storage_week_sales: int,       # 보판_최근7일체결량
                #  total_latest_date: str,        # 전체_최근체결날짜
                #  total_latest_price: int,       # 전체_최근체결금액
                #  total_week_sales: int,         # 전체_최근7일체결량
                #  option_name: str = None):  

    # @parameterized.expand([(
    #         Product(url="https://kream.co.kr/products/430299"),
    #         (Filter(category1="신발", category2="스니커즈", 
    #             keyword="조던", sort_by="남성 인기순", min_margin=10,
    #             exclude_storage=True, exclude_release_above=False, 
    #             exclude_no_release=False, min_total_sales=5, min_period_sales=5,
    #             min_immediate_price=200000, max_immediate_price=1000000, size_options="260,265,270")
    #             )
    #             ),
    #         ])
    # def test_click_harvest(self, product: Product, filter: Filter):
    #     try:
    #         ## 로그인 진행
    #         self.open("https://kream.co.kr/login")
    #         self.type('input[type="email"]', "ehdwnsqkqhek@naver.com")
    #         self.type('input[type="password"]', "Tls1169511!")
    #         self.click('button[type="submit"]')
    #         self.wait(1)
    #         self.open(product.url)
    #         product.name = self.get_text('main-title-container p.title')
    #         product.url = self.get_current_url()
    #         product.product_id = url.split("/")[-1]
    #         product.category = filter.category1 + "/" + filter.category2
    #         product.brand

    #     except Exception as e:
    #         print(f"테스트 실행 중 오류 발생: {str(e)}")


if __name__ == "__main__":
    pytest.main(['tests/function.py', '-s', '-v', '--maximize'])

## pytest options
# -v  # Verbose mode. Prints the full name of each test and shows more details.
# -q  # Quiet mode. Print fewer details in the console output when running tests.
# -x  # Stop running the tests after the first failure is reached.
# -n=NUM  # Multithread the tests using that many threads. (Speed up test runs!)
# -s  # See print statements. (Should be on by default with pytest.ini present.)
# --junit-xml=report.xml  # Creates a junit-xml report after tests finish.
# --pdb  # If a test fails, enter Post Mortem Debug Mode. (Don't use with CI!)
# --trace  # Enter Debug Mode at the beginning of each test. (Don't use with CI!)

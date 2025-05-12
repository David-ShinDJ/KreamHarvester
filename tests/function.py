## 크롤링에서 자주사용하는 SeleniumBase 함수선언하기
from seleniumbase import BaseCase
from parameterized import parameterized
import pytest
from src.models.filter import Filter
from src.models.product import Product
from src.utils.pause import pause
from src.models.pointer import Pointer
## FIXME: 이슈모음
## 1. typing 인식안돼는 이슈 존재
        # self.click("button.btn_search.header-search-button.search-button-margin")
         # ## typing 인식안돼는 이슈 존재
        # self.type('input[type="text"]', "조던 + \n")
## 2. 크림사이트에서 보여지는 텍스트 "L" 인식이 되지않는 이슈있음 --> tag 를 구체화하니까 해결됌
        # def test_click_size(self, url, size_options):
        #     try:
        #         ## 로그인 진행
        #         self.open("https://kream.co.kr/login")
        #         self.type('input[type="email"]', "ehdwnsqkqhek@naver.com")
        #         self.type('input[type="password"]', "Tls1169511!")
## 3. data; 페이지가 로드되는경우 잘못된요소를 클릭하거나 이동하면발생함 
    # self.wait 페이지로드시 필요한 함수, self.sleep 스크립트작업을 아예끄는방식 모든 작업이 끝날떄 sleepp 사용해야함
## 4. 단어의 띄어쓰기있는경우 
    #self.click('li.sorting_item p:contains("%s")' % test_sorting) %s 문법사용해야함
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
    # @parameterized.expand([
    #     Pointer(index=1),
    #     Pointer(index=5),
    #     Pointer(index=10),
    #     Pointer(index=20),
    #     Pointer(index=40),
    # ])

    # def test_pointer(self, pointer: Pointer):
    #     """ 제품 검색 및 클릭 """
    #     try:
    #         self.open("https://kream.co.kr/search")
    #         text = self.get_text(f'div[data-result-index="{pointer.index}"]')
    #         text_list = text.split("\n")# 디버깅용 출력
    #         pointer.product_trade_volume = text_list[0].replace("거래 ", "")  # "거래 1.3만" -> "1.3만"
    #         pointer.product_brand = text_list[1]  # "Asics"
    #         pointer.product_name = text_list[3]   # "아식스 젤 소노마 15-50 블랙"
    #         pointer.product_immediate_buy_price_average = text_list[5].replace("원", "").replace(",", "")  # "145,000원" -> "145000"
    #         pointer.product_likes = text_list[7]  # "3.2만"
    #         pointer.product_reviews = text_list[8]  # "236"
    #     except Exception as e:
    #         print(f"제품 검색 테스트 실패: {e}")
    #     finally:
    #         print(f"포인터 정보: {pointer}")

    @parameterized.expand([
    # ("https://kream.co.kr/search?keyword=지갑", 10),
    # ("https://kream.co.kr/search?keyword=에어포스", 20),
    ("https://kream.co.kr/search?keyword=오버핏티셔츠", 50),
    ])
    ## FIXME: data; 페이지 팅기는 이슈 1. wait 안돼고 바로 로드되는경우 없는 요소를 클릭하는경우 2. 스크롤 문제로인해서 
#인덱스 5에 해당하는 요소를 찾을 수 없음, 다음 인덱스로 진행
## click 이동하는경우 index 넘버가 변경된다 크림사이트는 !!
## 오류 분기해서 생각해서 코드 다시짜기!! 인덱스가 진짜 없는 경우 , 인덱스가 있는데 스크롤이 안된경우
    def test_extract_products(self, keyword_url, numbers):
        self.open(keyword_url)
        i = 0
        while i < numbers:
            try:
                # 실제 상품 요소만 찾기
                products = self.find_elements('div.search_result_item.product')
                if i >= len(products):
                    print(f"더 이상 상품이 없습니다. 현재 인덱스: {i}")
                    break
                    
                # i번째 상품 클릭
                products[i].click()
                self.wait(1)
                print(self.get_current_url())
                self.go_back()
                self.wait(1)
                i += 1  # 성공했을 때만 i 증가
            except Exception as e:
                print(f"오류발생 {str(e)}")
                i += 1  # 오류가 발생해도 i를 증가시켜서 다음 인덱스로 넘어감
                    
# ## TODO: 추출기에서 필요한 정보만 추출하기 필요데이터선정하기
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
    #         (Product(),
    #         (Filter(category1="아우터", category2="바람막이", 
    #             keyword="바람막이", sort_by="인기순", min_margin=20,
    #             exclude_storage=False, exclude_release_above=False, 
    #             exclude_no_release=True, min_total_sales=2, min_period_sales=3,
    #             min_immediate_price=100000, max_immediate_price=1000000, size_options="모든사이즈")),
    #         )
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
# --html=report.html  # Creates a detailed pytest-html report after tests finish.
# --co | --collect-only  # Show what tests would get run. (Without running them)
# --co -q  # (Both options together!) - Do a dry run with full test names shown.
# -n=NUM  # Multithread the tests using that many threads. (Speed up test runs!)
# -s  # See print statements. (Should be on by default with pytest.ini present.)
# --junit-xml=report.xml  # Creates a junit-xml report after tests finish.
# --pdb  # If a test fails, enter Post Mortem Debug Mode. (Don't use with CI!)
# --trace  # Enter Debug Mode at the beginning of each test. (Don't use with CI!)

## SeleniumBase options
# --browser=BROWSER  # (The web browser to use. Default: "chrome".)
# --chrome  # (Shortcut for "--browser=chrome". On by default.)
# --edge  # (Shortcut for "--browser=edge".)
# --firefox  # (Shortcut for "--browser=firefox".)
# --safari  # (Shortcut for "--browser=safari".)
# --settings-file=FILE  # (Override default SeleniumBase settings.)
# --env=ENV  # (Set the test env. Access with "self.env" in tests.)
# --account=STR  # (Set account. Access with "self.account" in tests.)
# --data=STRING  # (Extra test data. Access with "self.data" in tests.)
# --var1=STRING  # (Extra test data. Access with "self.var1" in tests.)
# --var2=STRING  # (Extra test data. Access with "self.var2" in tests.)
# --var3=STRING  # (Extra test data. Access with "self.var3" in tests.)
# --variables=DICT  # (Extra test data. Access with "self.variables".)
# --user-data-dir=DIR  # (Set the Chrome user data directory to use.)
# --protocol=PROTOCOL  # (The Selenium Grid protocol: http|https.)
# --server=SERVER  # (The Selenium Grid server/IP used for tests.)
# --port=PORT  # (The Selenium Grid port used by the test server.)
# --cap-file=FILE  # (The web browser's desired capabilities to use.)
# --cap-string=STRING  # (The web browser's desired capabilities to use.)
# --proxy=SERVER:PORT  # (Connect to a proxy server:port as tests are running)
# --proxy=USERNAME:PASSWORD@SERVER:PORT  # (Use an authenticated proxy server)
# --proxy-bypass-list=STRING # (";"-separated hosts to bypass, Eg "*.foo.com")
# --proxy-pac-url=URL  # (Connect to a proxy server using a PAC_URL.pac file.)
# --proxy-pac-url=USERNAME:PASSWORD@URL  # (Authenticated proxy with PAC URL.)
# --proxy-driver  # (If a driver download is needed, will use: --proxy=PROXY.)
# --multi-proxy  # (Allow multiple authenticated proxies when multi-threaded.)
# --agent=STRING  # (Modify the web browser's User-Agent string.)
# --mobile  # (Use the mobile device emulator while running tests.)
# --metrics=STRING  # (Set mobile metrics: "CSSWidth,CSSHeight,PixelRatio".)
# --chromium-arg="ARG=N,ARG2"  # (Set Chromium args, ","-separated, no spaces.)
# --firefox-arg="ARG=N,ARG2"  # (Set Firefox args, comma-separated, no spaces.)
# --firefox-pref=SET  # (Set a Firefox preference:value set, comma-separated.)
# --extension-zip=ZIP  # (Load a Chrome Extension .zip|.crx, comma-separated.)
# --extension-dir=DIR  # (Load a Chrome Extension directory, comma-separated.)
# --disable-features="F1,F2"  # (Disable features, comma-separated, no spaces.)
# --binary-location=PATH  # (Set path of the Chromium browser binary to use.)
# --driver-version=VER  # (Set the chromedriver or uc_driver version to use.)
# --sjw  # (Skip JS Waits for readyState to be "complete" or Angular to load.)
# --wfa  # (Wait for AngularJS to be done loading after specific web actions.)
# --pls=PLS  # (Set pageLoadStrategy on Chrome: "normal", "eager", or "none".)
# --headless  # (The default headless mode. Linux uses this mode by default.)
# --headless1  # (Use Chrome's old headless mode. Fast, but has limitations.)
# --headless2  # (Use Chrome's new headless mode, which supports extensions.)
# --headed  # (Run tests in headed/GUI mode on Linux OS, where not default.)
# --xvfb  # (Run tests using the Xvfb virtual display server on Linux OS.)
# --xvfb-metrics=STRING  # (Set Xvfb display size on Linux: "Width,Height".)
# --locale=LOCALE_CODE  # (Set the Language Locale Code for the web browser.)
# --interval=SECONDS  # (The autoplay interval for presentations & tour steps)
# --start-page=URL  # (The starting URL for the web browser when tests begin.)
# --archive-logs  # (Archive existing log files instead of deleting them.)
# --archive-downloads  # (Archive old downloads instead of deleting them.)
# --time-limit=SECONDS  # (Safely fail any test that exceeds the time limit.)
# --slow  # (Slow down the automation. Faster than using Demo Mode.)
# --demo  # (Slow down and visually see test actions as they occur.)
# --demo-sleep=SECONDS  # (Set the wait time after Slow & Demo Mode actions.)
# --highlights=NUM  # (Number of highlight animations for Demo Mode actions.)
# --message-duration=SECONDS  # (The time length for Messenger alerts.)
# --check-js  # (Check for JavaScript errors after page loads.)
# --ad-block  # (Block some types of display ads from loading.)
# --host-resolver-rules=RULES  # (Set host-resolver-rules, comma-separated.)
# --block-images  # (Block images from loading during tests.)
# --do-not-track  # (Indicate to websites that you don't want to be tracked.)
# --verify-delay=SECONDS  # (The delay before MasterQA verification checks.)
# --ee | --esc-end  # (Lets the user end the current test via the ESC key.)
# --recorder  # (Enables the Recorder for turning browser actions into code.)
# --rec-behave  # (Same as Recorder Mode, but also generates behave-gherkin.)
# --rec-sleep  # (If the Recorder is enabled, also records self.sleep calls.)
# --rec-print  # (If the Recorder is enabled, prints output after tests end.)
# --disable-cookies  # (Disable Cookies on websites. Pages might break!)
# --disable-js  # (Disable JavaScript on websites. Pages might break!)
# --disable-csp  # (Disable the Content Security Policy of websites.)
# --disable-ws  # (Disable Web Security on Chromium-based browsers.)
# --enable-ws  # (Enable Web Security on Chromium-based browsers.)
# --enable-sync  # (Enable "Chrome Sync" on websites.)
# --uc | --undetected  # (Use undetected-chromedriver to evade bot-detection.)
# --uc-cdp-events  # (Capture CDP events when running in "--undetected" mode.)
# --log-cdp  # ("goog:loggingPrefs", {"performance": "ALL", "browser": "ALL"})
# --remote-debug  # (Sync to Chrome Remote Debugger chrome://inspect/#devices)
# --ftrace | --final-trace  # (Debug Mode after each test. Don't use with CI!)
# --dashboard  # (Enable the SeleniumBase Dashboard. Saved at: dashboard.html)
# --dash-title=STRING  # (Set the title shown for the generated dashboard.)
# --enable-3d-apis  # (Enables WebGL and 3D APIs.)
# --swiftshader  # (Chrome "--use-gl=angle" / "--use-angle=swiftshader-webgl")
# --incognito  # (Enable Chrome's Incognito mode.)
# --guest  # (Enable Chrome's Guest mode.)
# --dark  # (Enable Chrome's Dark mode.)
# --devtools  # (Open Chrome's DevTools when the browser opens.)
# --rs | --reuse-session  # (Reuse browser session for all tests.)
# --rcs | --reuse-class-session  # (Reuse session for tests in class.)
# --crumbs  # (Delete all cookies between tests reusing a session.)
# --disable-beforeunload  # (Disable the "beforeunload" event on Chrome.)
# --window-position=X,Y  # (Set the browser's starting window position.)
# --window-size=WIDTH,HEIGHT  # (Set the browser's starting window size.)
# --maximize  # (Start tests with the browser window maximized.)
# --screenshot  # (Save a screenshot at the end of each test.)
# --no-screenshot  # (No screenshots saved unless tests directly ask it.)
# --visual-baseline  # (Set the visual baseline for Visual/Layout tests.)
# --wire  # (Use selenium-wire's webdriver for replacing selenium webdriver.)
# --external-pdf  # (Set Chromium "plugins.always_open_pdf_externally":True.)
# --timeout-multiplier=MULTIPLIER  # (Multiplies the default timeout values.)
# --list-fail-page  # (After each failing test, list the URL of the failure.)


# 1. 예외 처리 (try-except 블록 사용):

# 예외 처리 블록을 사용하여 요소 클릭, 검색, 로딩 대기 등 오류가 발생할 수 있는 코드를 감싸세요.
# 특정 예외 (예: NoSuchElementException, TimeoutException) 를 처리하고, 오류 메시지를 출력하거나 로깅하고, 다음 단계로 진행하도록 코드를 작성하세요.
# Python

# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException, TimeoutException
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# driver = webdriver.Chrome()
# driver.get("your_url")

# try:
#     # 요소가 나타날 때까지 최대 10초 대기
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "your_element_id"))
#     )
#     element.click()
# except NoSuchElementException:
#     print("요소를 찾을 수 없습니다.")
# except TimeoutException:
#     print("요소 로딩 시간 초과.")
# except Exception as e:
#     print(f"예상치 못한 오류 발생: {e}")

# # 다음 크롤링 단계 진행
# 2. 명시적 대기 (Explicit Waits) 사용:

# time.sleep() 대신 WebDriverWait와 expected_conditions를 사용하여 요소가 나타나거나 특정 조건이 충족될 때까지 기다리세요.
# 최대 대기 시간을 설정하고, 시간 초과 시 예외를 처리하세요.
# 3. 요소 존재 여부 확인:

# find_elements() 메서드를 사용하여 요소가 존재하는지 확인하고, 존재하는 경우에만 클릭하거나 처리하세요.
# Python

# elements = driver.find_elements(By.ID, "your_element_id")
# if elements:
#     elements[0].click()
# 4. 반복 로직 구현:

# 일정 횟수만큼 재시도하거나 특정 조건이 충족될 때까지 반복하는 로직을 구현하세요.
# Python

# retries = 3
# for i in range(retries):
#     try:
#         element = driver.find_element(By.ID, "your_element_id")
#         element.click()
#         break  # 성공하면 반복 종료
#     except NoSuchElementException:
#         if i < retries - 1:
#             print(f"재시도 {i + 1}...")
#             time.sleep(2)  # 재시도 전 대기
#         else:
#             print("최대 재시도 횟수 초과.")
# 5. 페이지 로딩 상태 확인:

# driver.execute_script("return document.readyState")를 사용하여 페이지 로딩 상태를 확인하고 완료될 때까지 대기하세요.
# 6. 오류 로깅 및 알림:

# 오류 메시지를 파일이나 데이터베이스에 로깅하여 나중에 분석하고 디버깅할 수 있도록 하세요.
# 오류 발생 시 이메일이나 Slack 등으로 알림을 보내는 기능을 추가하세요.
# 7. 헤드리스 모드 사용:

# 크롬 드라이버 옵션에서 헤드리스 모드를 사용하여 브라우저 창을 표시하지 않고 크롤링을 실행해 보세요.
# Python

# options = webdriver.ChromeOptions()
# options.add_argument("--headless")
# driver = webdriver.Chrome(options=options)
# 8. User-Agent 설정:

# 크롤링 봇으로 감지되는 것을 방지하기 위해 User-Agent를 설정하세요.
# Python

# options.add_argument("user-agent=your_user_agent")
# 이러한 방법들을 조합하여 사용하면 웹 크롤링 프로그램을 보다 안정적으로 만들 수 있습니다.
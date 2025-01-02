from seleniumbase import BaseCase
from parameterized import parameterized
from utils.pause import pause_while
from models.product import Product, ProductInfo
from excels.excel import Excel
import time, re, os

## 추출한 데이터 다시 정의하기

product_sample = Product(
    name="노스페이스 온 볼 자켓 블랙",
    url="https://kream.co.kr/products/178681?fetchRelated=true",
    option="모든 사이즈",
    ipp=152000,
    ssp=164000,
    info=ProductInfo(rtp=176000, rpc=9000, rp=249000, mn="NJ3NP55A/NJ3NQ53A/NJ3NQ53E", rd="-", rc="black")
)

class Collect(BaseCase):
    def setUp(self):
        super().setUp()
        self.excel = Excel()
    
    def tearDown(self):
        self.excel.save()
        super().tearDown()

    @parameterized.expand([
        ("패딩", 20),
        # ("크롬하츠", 1),
        # ("지갑", 3),
        # ("조던", 4)
    ])
    def test_collect(self, test_keyword: str, extract_number: int):
        try:
            self.open(f"https://kream.co.kr/search?keyword={test_keyword}")
            collected_indices = set()  # 수집한 인덱스 추적

            for i in range(extract_number):
                product_selector = f'div.search_result_list div.search_result_item.product[data-result-index="{i}"]'
                next_prodcut_selector = f'div.search_result_list div.search_result_item.product[data-result-index="{i+1}"]'
                
                # 이미 수집한 인덱스면 스킵
                if i in collected_indices:
                    print(f"인덱스 {i}는 이미 수집되었습니다. 건너뜁니다.")
                    continue
                
                # 스크롤 횟수 카운터 초기화
                scroll_count = 0
                
                while not self.is_element_visible(product_selector):
                    if self.is_element_visible(next_prodcut_selector):
                        product_selector = next_prodcut_selector
                        break
                    
                    # 스크롤 5회 이상이면 탈출
                    if scroll_count >= 3:
                        print(f"인덱스 {i}의 상품을 찾기 위해 {scroll_count}회 스크롤했지만 찾지 못했습니다. 다음 상품으로 넘어갑니다.")
                        break
                        
                    self.execute_script("window.scrollBy(0, 100);")
                    scroll_count += 1
                    self.sleep(0.5)
                    

                self.click(product_selector)
                self.sleep(0.5)

                name = self.get_text("div.main-title-container p.sub-title")
                url = self.get_current_url()
                if self.is_element_visible('div.product_figure_wrap.lg span.title-txt'):
                    option = self.get_text('div.product_figure_wrap.lg span.title-txt')
                else:
                    option = None
                ipp = int(
                    re.sub(r'[^\d]', '', self.get_text('div.price-text-container p.text-lookup.price.display_paragraph')))
                ssp_elements = self.find_elements('div.btn_wrap div.price em')
                ssp = int(re.sub(r'[^\d]', '', ssp_elements[1].text))
                texts_element = self.get_text('div.product_info_wrap dl.detail-product-container')
                info = get_info(texts_element)
                product = Product(name, url, option, ipp, ssp, info)
                self.excel.add_product(product)
                self.go_back()
            pause_while()
        
        except Exception as e:
            print(f"컬렉트 실패: {e}")


def get_info(text_elements: str) -> ProductInfo:
    lines = text_elements.split('\n')
    values = [lines[i] for i in [1, 2, 4, 6, 8, 10]]
    
    try:
        # 가격 문자열에서 숫자만 추출
        rtp_str = re.sub(r'[^\d]', '', values[0])
        rtp = int(rtp_str) if rtp_str else 0  # 빈 문자열이면 0으로 처리
        
        # 가격변동 문자열 처리
        rpc_str = values[1]
        if '▼' in rpc_str:  # 가격 하락
            number_str = re.sub(r'[^\d]', '', rpc_str.split()[0])
            rpc = -int(number_str) if number_str else 0
        elif '▲' in rpc_str:  # 가격 상승
            number_str = re.sub(r'[^\d]', '', rpc_str.split()[0])
            rpc = int(number_str) if number_str else 0
        else:  # 변동 없음
            rpc = 0
        
        # 발매가 처리
        rp_str = re.sub(r'[^\d]', '', values[2])
        rp = int(rp_str) if rp_str else 0  # 빈 문자열이면 0으로 처리
        
    except Exception as e:
        print(f"가격 정보 처리 중 오류 발생: {e}")
        print(f"처리하려던 값들: {values}")
        rtp, rpc, rp = 0, 0, 0  # 오류 발생시 기본값 설정
    
    return ProductInfo(
        rtp=rtp,          # 최근거래가
        rpc=rpc,          # 최근가격변동
        rp=rp,            # 발매가
        mn=values[3],     # 모델번호
        rd=values[4],     # 출시일
        rc=values[5]      # 대표색상
    )

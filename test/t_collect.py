from seleniumbase import BaseCase
from parameterized import parameterized
from utils.pause import pause_while
from models.product import Product, ProductInfo
from excels.excel import Excel
import time, re, os

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
        ("패딩", 2),
        # ("크롬하츠", 1),
        # ("지갑", 3),
        # ("조던", 4)
    ])
    def test_collect(self, test_keyword: str, number: int):
        try:
            self.open(f"https://kream.co.kr/search?keyword={test_keyword}")
            self.click(f'div.search_result_list div.search_result_item.product[data-result-index="{number}"]')
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
            print(product, product.info)
            self.excel.add_product(product)
            self.go_back()
            pause_while()
        
        except Exception as e:
            print(f"컬렉트 실패: {e}")


def get_info(text_elements: str) -> ProductInfo:
    lines = text_elements.split('\n')
    values = [lines[i] for i in [1, 2, 4, 6, 8, 10]]
    
    # 가격 문자열에서 숫자만 추출
    rtp = int(re.sub(r'[^\d]', '', values[0]))  # 최근거래가
    
    # 가격변동 문자열 처리
    rpc_str = re.sub(r'[^\d.]', '', values[1])
    rpc = int(float(rpc_str.split()[0]) if rpc_str else 0)  # 최근가격변동
    
    # 발매가 처리
    rp = int(re.sub(r'[^\d]', '', values[2]))  # 발매가
    
    return ProductInfo(
        rtp=rtp,          # 최근거래가
        rpc=rpc,          # 최근가격변동
        rp=rp,            # 발매가
        mn=values[3],     # 모델번호
        rd=values[4],     # 출시일
        rc=values[5]      # 대표색상
    )

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


class TestLogin(BaseCase):
    def test_py(self):
        try:
            self.open("https://kream.co.kr/")
            self.click('a:contains("SHOP")')
            self.wait_for_element("div.content-container")
            # 필터모달 열기
            self.click('p.text-group span:contains("카테고리")')
            self.click('div.shop-filter-sections.category.expanded span.collapse-icon')
            self.click('div.shop-filter-sections.gender.expanded span.collapse-icon')
            self.click('div.shop-filter-sections.benefits.expanded span.collapse-icon')
            self.click('div.shop-filter-sections.tag_id\[size\] span.collapse-icon')
            # self.hover('filter-section-list.tag_id[size] p.contains("%s")' % "의류")
            # self.click('p.text-group span:contains("%s")' % "XL")
            pause_while(auto_mode=False)
        except Exception as e:
            print(f"로그인 실패: {e}")
import random
## TODO: Filter 랜덤케이스 테스트가 통과완료 -> 100% 테스트 성공은 아니지만 추후에 failtest 모으기 !!
from parameterized import parameterized
from seleniumbase import BaseCase
from utils.data_manager import DataManager
from src.utils.pause import pause_while
## 테스트케이스랜덤발생
data_manager = DataManager()
cate_dic = data_manager.json_to_dictionary('category')
test_cate = random.choice(list(cate_dic.keys()))
test_cate_detail = random.choice(cate_dic[test_cate])

gender_dic = data_manager.json_to_dictionary('gender')
test_gender = random.choice(gender_dic["성별"])

color_dic = data_manager.json_to_dictionary('color')
test_color = random.choice(color_dic["색상"])

benefit_dictionary = data_manager.json_to_dictionary('benefit')
test_benefit = random.choice(list(benefit_dictionary.keys()))
test_benefit_detail = random.choice(benefit_dictionary[test_benefit])

brand_dic = data_manager.json_to_dictionary('brand')
test_brand = random.choice(list(brand_dic.keys()))
test_brand_detail = random.choice(brand_dic[test_brand])

collection_dic = data_manager.json_to_dictionary('collection')
test_collection = random.choice(collection_dic["컬렉션"])

size_dictionary = data_manager.json_to_dictionary('size')
test_size = random.choice(list(size_dictionary.keys()))
test_size_detail = random.choice(size_dictionary[test_size])

price_dic = data_manager.json_to_dictionary('price')
test_price = random.choice(price_dic["가격대"])

sorting_list = data_manager.json_to_list('sorting')
test_sorting = random.choice(sorting_list)

print(test_cate, test_cate_detail, test_gender, test_color, test_benefit, test_benefit_detail, test_brand, test_brand_detail, test_collection, test_size,  test_size_detail, test_price, test_sorting)
## Test Case
"""
    ("아우터", "패딩", "남성", "블랙", "혜택", "모두 선택", "N", "Nike", "Luxury", "의류", "XL", "30-50만원", "남성 인기순"),
    ("신발", "스니커즈", "여성", "아이보리", "할인율", "30% 이하", "T", "Tabi", "Contemporary", "신발", "240", "20만원대", "여성 인기순")
"""
        # (test_cate_detail, test_gender, test_color, test_benefit, test_benefit_detail, test_brand, test_collection, test_size, test_size_detail, test_price, test_sorting),
class Filter(BaseCase):
    @parameterized.expand([
            ("아우터", "패딩", "남성", "블랙", "혜택", "모두 선택", "N", "Nike", "Luxury", "의류", "XL", "30-50만원", "남성 인기순"),
            # ("신발", "스니커즈", "여성", "아이보리", "할인율", "30% 이하", "T", "Tabi", "Contemporary", "신발", "240", "20만원대", "여성 인기순"),
            # (test_cate, test_cate_detail, test_gender, test_color, test_benefit, test_benefit_detail, test_brand, test_brand_detail, test_collection, test_size,  test_size_detail, test_price, test_sorting)

    ])
    def test_set_filter(self, test_cate: str ,test_category_detail: str, test_gender: str, test_color: str, test_benefit: str, test_benefit_detail: str, test_brand: str, test_brand_detail: str, test_collection: str, test_size: str, test_size_detail: str, test_price: str, test_sorting: str):
        try:
            self.open("https://kream.co.kr/")
            self.click('a:contains("SHOP")')
            self.wait_for_element("div.content-container")
            # 필터모달 열기
            self.click('p.text-group span:contains("카테고리")')
            ## 필터리셋시키기
            self.click('div.shop-filter-sections.gender.expanded span.collapse-icon')
            self.click('div.shop-filter-sections.benefits.expanded span.collapse-icon')
            ## 카테고리필터키기
            self.click('div.shop-filter-sections button:contains("더보기")')
            ## 카테고리선택 -> 모두 선택 카테고리에서는 없음
            self.hover('div.shop-filter-sections.category.expanded div.section_titles p:contains("%s")' % test_cate)
            self.click('button.filter_button.tint span:contains("%s")' % test_category_detail)
            self.click('div.shop-filter-sections.category.expanded span.collapse-icon')
            self.sleep(1)
            ## 성별선택
            if self.is_element_present('div.shop-filter-sections.gender'):
                self.click('div.shop-filter-sections.gender span.collapse-icon')
                if self.is_element_visible('p.text-group span:contains("%s")' % test_gender):
                    self.click('p.text-group span:contains("%s")' % test_gender)
                self.click('div.shop-filter-sections.gender.expanded span.collapse-icon')
                self.sleep(1)

            ## 색상선택
            if self.is_element_present('div.shop-filter-sections.color'):
                self.click('div.shop-filter-sections.color span.collapse-icon')
                if self.is_element_visible('div.shop-filter-sections.color p:contains("%s")' % test_color):
                    self.click('div.shop-filter-sections.color p:contains("%s")' % test_color)
                self.click('div.shop-filter-sections.color.expanded span.collapse-icon')
                self.sleep(1)
            
            ## 혜택/할인 선택
            if self.is_element_present('div.shop-filter-sections.benefits'):
                self.click('div.shop-filter-sections.benefits span.collapse-icon')
                if test_benefit_detail == "모두 선택":
                    self.click("//p[contains(text(), '%s')]/following-sibling::button[@class='btn_multiple']" % test_benefit)
                else:
                    if self.is_element_visible('div.shop-filter-sections.benefits span:contains("%s")' % test_benefit_detail):
                        self.click('div.shop-filter-sections.benefits span:contains("%s")' % test_benefit_detail)
                self.click('div.shop-filter-sections.benefits.expanded span.collapse-icon')
                self.sleep(1)
            ## 브랜드 선택
            if self.is_element_present('div.shop-filter-sections.brand'):
                self.click('div.shop-filter-sections.brand span.collapse-icon')
                if self.is_element_visible('div.filter-section-list.brand div.section_titles p.title:contains("%s")' % test_brand):
                    self.hover('div.section_contents span:contains("%s")' % test_brand_detail)
                    self.click('div.section_contents span:contains("%s")' % test_brand_detail)
                else:
                    pass
                self.click('div.shop-filter-sections.brand.expanded span.collapse-icon')
                self.sleep(1)

            ## 컬렉션 선택
            if self.is_element_visible('div.shop-filter-sections.collection'):
                self.click('div.shop-filter-sections.collection span.collapse-icon')
                if self.is_element_present('div.section_contents span:contains("%s")' % test_collection):
                    self.hover_and_click('div.section_contents span:contains("%s")' % test_collection)
                else:
                    pass
                self.click('div.shop-filter-sections.collection.expanded span.collapse-icon')
                self.sleep(1)
    
            ## 사이즈 선택  
            if self.is_element_present('div.shop-filter-sections.tag_id\[size\]'):
                self.click('div.shop-filter-sections.tag_id\[size\] span.collapse-icon')
                if self.is_element_visible('div.filter-section-list.tag_id\[size\] div.section_titles p.title:contains("%s")' % test_size):
                    self.click('div.section_contents span:contains("%s")' % test_size_detail)
                self.click('div.shop-filter-sections.tag_id\[size\].expanded span.collapse-icon')  
                self.sleep(1)
            
            ## 가격대 선택
            if self.is_element_present('div.shop-filter-sections.price'):
                self.click('div.shop-filter-sections.price span.collapse-icon')
                self.hover_and_click('div.shop-filter-sections.price div.vue-slider-rail', 'button.filter_button.tint span:contains("%s")' % test_price)
                self.click('div.shop-filter-sections.price.expanded span.collapse-icon')
                self.sleep(1)
            ## 필터적용
            self.click('a.btn.full.solid')

            ## sorting 
            if test_sorting == "인기순":
                pass
            else:
                self.click('div.content-container button.sorting_title')
                self.click('li.sorting_item p:contains("%s")' % test_sorting)
            pause_while()
            
            # 또는 대신 명시적 대기 사용
        except Exception as e:

            print(f"필터적용 실패: {e}")

from seleniumbase import BaseCase
from parameterized import parameterized
from src.utils.pause import pause_while
from src.models.product import Product, ProductInfo
from src.utils.excel import Excel

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
        ("패딩", 1),
        # ("크롬하츠", 1),
        # ("지갑", 3),
        # ("조던", 4)
    ])
    def test_collect(self, test_keyword: str, number: int):
        try:
            self.open("https://kream.co.kr/login")
            self.type('input[type="email"]', "ehdwnsqkqhek@naver.com")
            self.type('input[type="password"]', "Tls1169511!")
            self.click('button[type="submit"]')
            self.sleep(1)
            self.click("button.btn_search")
            ## 검색 및 Press Enter
            self.type('input[type="text"]', test_keyword + "\n")
            self.sleep(1)
            self.click(f'div.search_result_list div.search_result_item.product[data-result-index="{number}"]')
            ## 모든 사이즈 옵션이 활성화된경우 클릭하기
            if self.is_element_present('div.product_figure_wrap.md'):
                self.click('div.button-container a.btn_size')
                self.is_element_present('div.modal-layer div.content.layer-detail-size-select-content')
                size_option = self.get_text('div.modal-layer div.content.layer-detail-size-select-content')
                print(size_option)
            else:
                self.click('div.button-container a.btn_size')
                self.is_element_present('div.modal-layer div.content.layer-detail-size-select-content')
                size_option = self.get_text('div.modal-layer div.content.layer-detail-size-select-content')
                print(size_option)
            pause_while()
            # name = self.get_text("div.main-title-container p.sub-title")
            # url = self.get_current_url()
            # if self.is_element_visible('div.product_figure_wrap.lg span.title-txt'):
            #     option = self.get_text('div.product_figure_wrap.lg span.title-txt')
            # else:
            #     option = None
            # ipp = int(
            #     re.sub(r'[^\d]', '', self.get_text('div.price-text-container p.text-lookup.price.display_paragraph')))
            # ssp_elements = self.find_elements('div.btn_wrap div.price em')
            # ssp = int(re.sub(r'[^\d]', '', ssp_elements[1].text))
            # texts_element = self.get_text('div.product_info_wrap dl.detail-product-container')
            # info = get_info(texts_element)
            # product = Product(name, url, option, ipp, ssp, info)
            # self.excel.add_product(product)
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

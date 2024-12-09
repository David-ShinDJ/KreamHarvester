import random
## TODO: Filter 랜덤케이스 테스트가 통과완료 -> 100% 테스트 성공은 아니지만 추후에 failtest 모으기 !!
from parameterized import parameterized
from seleniumbase import BaseCase
from utils.data_manager import DataManager
from utils.pause import pause_while
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
test_brand = random.choice(brand_dic["브랜드"])

collection_dic = data_manager.json_to_dictionary('collection')
test_collection = random.choice(collection_dic["컬렉션"])

size_dictionary = data_manager.json_to_dictionary('size')
test_size = random.choice(list(size_dictionary.keys()))
test_size_detail = random.choice(size_dictionary[test_size])

price_dic = data_manager.json_to_dictionary('price')
test_price = random.choice(price_dic["가격"])

sorting_list = data_manager.json_to_list('sorting')
test_sorting = random.choice(sorting_list)

print(test_cate, test_cate_detail, test_gender, test_color, test_benefit, test_benefit_detail, test_brand, test_collection, test_size,  test_size_detail, test_price, test_sorting)
## Test Case
"""
    ("아우터", "패딩", "남성", "블랙", "혜택", "모두 선택", "Nike", "Luxury", "의류", "XL", "30-50만원", "남성 인기순"),
    ("신발", "스니커즈", "여성", "아이보리", "할인율", "30% 이하", "Tabi", "Contemporary", "신발", "240", "20만원대", "여성 인기순")
"""
        # (test_cate_detail, test_gender, test_color, test_benefit, test_benefit_detail, test_brand, test_collection, test_size, test_size_detail, test_price, test_sorting),
class Filter(BaseCase):
    @parameterized.expand([
            ("아우터", "패딩", "남성", "블랙", "혜택", "모두 선택", "Nike", "Luxury", "의류", "XL", "30-50만원", "남성 인기순"),
    ])
    def test_set_filter(self, test_cate: str ,test_category_detail: str, test_gender: str, test_color: str, test_benefit: str, test_benefit_detail: str, test_brand: str, test_collection: str, test_size: str, test_size_detail: str, test_price: str, test_sorting: str):
        try:
            self.open("https://kream.co.kr/")
            self.click('a:contains("SHOP")')
            self.wait_for_element("div.content-container")
            # 필터모달 열기
            self.click('p.text-group span:contains("카테고리")')
            ## 필터리셋시키기
            self.click('div.shop-filter-sections.category.expanded span.collapse-icon')
            self.click('div.shop-filter-sections.gender.expanded span.collapse-icon')
            self.click('div.shop-filter-sections.benefits.expanded span.collapse-icon')
            ## 카테고리필터키기
            self.click('div.shop-filter-sections.category span.collapse-icon')
            self.click('div.shop-filter-sections button:contains("더보기")')

            ## 카테고리선택 -> 모두 선택 카테고리에서는 없음
            self.click('button.filter_button.tint span:contains("%s")' % test_category_detail)
            self.click('div.shop-filter-sections.category.expanded span.collapse-icon')

            self.sleep(1)

            ## 성별선택
            if self.is_element_present('div.shop-filter-sections.gender'):
                self.click('div.shop-filter-sections.gender span.collapse-icon')
                if self.is_element_visible('p.text-group span:contains("%s")' % test_gender):
                    self.click('p.text-group span:contains("%s")' % test_gender)
                self.click('div.shop-filter-sections.gender.expanded span.collapse-icon')

            ## 색상선택
            if self.is_element_present('div.shop-filter-sections.color'):
                self.click('div.shop-filter-sections.color span.collapse-icon')
                if self.is_element_visible('div.shop-filter-sections.color p:contains("%s")' % test_color):
                    self.click('div.shop-filter-sections.color p:contains("%s")' % test_color)
                self.click('div.shop-filter-sections.color.expanded span.collapse-icon')
            
            ## 혜택/할인 선택
            if self.is_element_present('div.shop-filter-sections.benefits'):
                self.click('div.shop-filter-sections.benefits span.collapse-icon')
                if test_benefit_detail == "모두 선택":
                    self.click("//p[contains(text(), '%s')]/following-sibling::button[@class='btn_multiple']" % test_benefit)
                else:
                    if self.is_element_visible('div.shop-filter-sections.benefits span:contains("%s")' % test_benefit_detail):
                        self.click('div.shop-filter-sections.benefits span:contains("%s")' % test_benefit_detail)
                self.click('div.shop-filter-sections.benefits.expanded span.collapse-icon')
            ## 브랜드 선택
            if self.is_element_present('div.shop-filter-sections.brand'):
                self.click('div.shop-filter-sections.brand span.collapse-icon')
                if self.is_element_visible('div.section_contents span:contains("%s")' % test_brand):
                    self.hover('div.section_contents span:contains("%s")' % test_brand)
                    self.click('div.section_contents span:contains("%s")' % test_brand)
                else:
                    pass
                self.click('div.shop-filter-sections.brand.expanded span.collapse-icon')
                self.sleep(1)

            ## 컬렉션 선택
            if self.is_element_visible('div.shop-filter-sections.collection'):
                self.click('div.shop-filter-sections.collection span.collapse-icon')
                if self.is_element_present('div.section_contents span:contains("%s")' % test_collection):
                    self.hover_click_element('div.section_contents span:contains("%s")' % test_collection)
                else:
                    pass
                self.click('div.shop-filter-sections.collection.expanded span.collapse-icon')
                self.sleep(1)
            ## 사이즈 선택  
            if self.is_element_present('div.shop-filter-sections.tag_id\[size\]'):
                self.click('div.shop-filter-sections.tag_id\[size\] span.collapse-icon')
                if self.is_element_visible('div.shop-filter-sections.tag_id\[size\] p.contains("%s")' % test_size):
                    self.click('p.text-group span:contains("%s")' % test_size_detail) 
                else:
                    pass
                self.click('div.shop-filter-sections.tag_id\[size\].expanded span.collapse-icon')  
            
            ## 가격대 선택
            if self.is_element_present('div.shop-filter-sections.price'):
                self.click('div.shop-filter-sections.price span.collapse-icon')
                self.hover_and_click('div.shop-filter-sections.price div.vue-slider-rail', 'button.filter_button.tint span:contains("%s")' % test_price)
                self.click('div.shop-filter-sections.price.expanded span.collapse-icon')
            ## 필터적용
            self.click('a.btn.full.solid')

            ## sorting 
            if test_sorting == "인기순":
                pass
            else:
                self.click('div.content-container button.sorting_title')
                self.click('li.sorting_item p:contains("%s")' % test_sorting)
            
            # 또는 대신 명시적 대기 사용
        except Exception as e:

            print(f"필터적용 실패: {e}")



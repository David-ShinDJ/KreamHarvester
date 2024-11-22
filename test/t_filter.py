import random
## TODO: Filter 항목에 따른 매칭 연결 시키기 카테고리:레고/ 사이즈항목 존재 -> 필터항목의 존재여부 확인후 클릭하기
from parameterized import parameterized
from seleniumbase import BaseCase
from utils.data_manager import DataManager
from utils.pause import pause_while
## 테스트케이스랜덤발생
data_manager = DataManager()
category_dictionary = data_manager.json_to_dictionary('category')
test_category = random.choice(list(category_dictionary.keys()))
test_category_detail = random.choice(category_dictionary[test_category])

gender_list = data_manager.json_to_list('gender')
test_gender = random.choice(gender_list)

color_list = data_manager.json_to_list('color')
test_color = random.choice(color_list)

benefit_dictionary = data_manager.json_to_dictionary('benefit')
test_benefit = random.choice(list(benefit_dictionary.keys()))
test_benefit_detail = random.choice(benefit_dictionary[test_benefit])

brand_list = data_manager.json_to_list('brand')
test_brand = random.choice(brand_list)

collection_list = data_manager.json_to_list('collection')
test_collection = random.choice(collection_list)

size_dictionary = data_manager.json_to_dictionary('size')
test_size = random.choice(list(size_dictionary.keys()))
test_size_detail = random.choice(size_dictionary[test_size])

price_list = data_manager.json_to_list('price')
test_price = random.choice(price_list)

print(test_category, test_category_detail, test_gender, test_color, test_benefit, test_benefit_detail, test_brand, test_collection, test_size,  test_size_detail, test_price)

class Filter(BaseCase):
    @parameterized.expand([
        ("아우터", "패딩", "남성", "블랙", "혜택", "모두 선택", "나이키"),
        ("신발", "모두 선택", "여성", "아이보리", "할인율", "30% 이하", "Tabi")
        # (test_category, test_category_detail, test_gender)
    ])
    def test_set_filter(self, test_category: str, test_category_detail: str, test_gender: str, test_color: str, test_benefit: str, test_benefit_detail: str, test_brand: str):
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

            ## 카테고리선택
            if test_category_detail == "모두 선택":
                self.click("//p[contains(text(), '%s')]/following-sibling::button[@class='btn_multiple']" % test_category)
            else:
                self.click('button.filter_button.tint span:contains("%s")' % test_category_detail)
            self.click('div.shop-filter-sections.category.expanded span.collapse-icon')

            ## 성별선택
            self.click('div.shop-filter-sections.gender span.collapse-icon')
            self.click('p.text-group span:contains("%s")' % test_gender)
            self.click('div.shop-filter-sections.gender.expanded span.collapse-icon')

            ## 색상선택
            self.click('div.shop-filter-sections.color span.collapse-icon')
            self.click('div.shop-filter-sections.color p:contains("%s")' % test_color)
            self.click('div.shop-filter-sections.color.expanded span.collapse-icon')
            ## 혜택/할인 선택
            self.click('div.shop-filter-sections.benefits span.collapse-icon')
            if test_benefit_detail == "모두 선택":
                self.click("//p[contains(text(), '%s')]/following-sibling::button[@class='btn_multiple']" % test_benefit)
            else:
                self.click('div.shop-filter-sections.benefits span:contains("%s")' % test_benefit_detail)
            self.click('div.shop-filter-sections.benefits.expanded span.collapse-icon')
            ## 브랜드 선택
            self.click('div.shop-filter-sections.brand span.collapse-icon')
            self.slow_scroll_to('shop-filter-sections brand expanded span:contains("%s")' % test_brand)
            self.click('filter-section-list.brand span:contains("%s")' % test_brand)
            self.click('div.shop-filter-sections.brand.expanded span.collapse-icon')

            pause_while(auto_mode=False)

            
            # 또는 대신 명시적 대기 사용
        except Exception as e:
            print(f"필터적용 실패: {e}")


"""
# self.click('div.shop-filter-sections button:contains("더보기")')
# self.wait_for_element('div.shop_filter_section_bubble span:contains("%s")' % "기타 가구/리빙")
# self.click('button.filter_button.tint span.title:contains("%s")' % category2)
# if basic_filter1 in ["성별","혜택/할인"]:
#     self.click('button.filter_button.tint span:contains("%s")' % basic_filter2)
# elif basic_filter1 == "색상":
#     self.click('div.shop-filter-sections.color svg')
#     self.click('div.filter-shortcut p:contains("%s")' % basic_filter2)
# elif basic_filter1 == "브랜드":
#     self.click('div.shop-filter-sections.brand svg')
#     self.click('div.filter_chip_group span:contains("%s")' % basic_filter2)
# elif basic_filter1 == "사이즈":
#     self.click('div.shop-filter-sections.tag_id[size] svg')
#     self.click('button.filter_button.tint span:contains("%s")' % basic_filter2)
# elif basic_filter1 == "가격대":
#     self.click('div.shop-filter-sections.price svg')
#     self.click('button.filter_button.tint span:contains("%s")' % basic_filter2)
# else:
#     pass
# self.click('a.btn.full.solid')
# self.click('li.menu span:contains("%s")' % test_category)
# self.click('li.menu span:contains("%s")' % test_category_detail)
# self.click('div.title_box span:contains("%s")' % test_basic_filter)
# self.wait_for_element('li.menu a.menu_link span.link_txt')
# self.click('li.menu p:contains("%s")' % test_category_detail)
# self.click('button.sorting_title')
# if data_filter != "추천순":
#     self.click('li.sorting_item p:contains("%s")' % test_data_filter)
"""

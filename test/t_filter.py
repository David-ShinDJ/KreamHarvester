import random
## TODO: Filter 항목에따른 매칭 연결시키기 카테고리:레고/ 사이즈항목 존재 x
from parameterized import parameterized
from seleniumbase import BaseCase
from constants import *
from utils import *
test_category = random.choice(list(config.category.keys()))
test_category_detail = random.choice(config.category[test_category])
test_basic_filter = random.choice(list(config.basic_filter.keys()))
test_basic_filter_detail = random.choice(config.basic_filter[test_basic_filter])
test_data_filter = random.choice(config.data_filter)
## fiter_modal 생성될떄 카테고리 성별 혜택/할인은 활성화 되어 있다
print(test_category_detail, test_basic_filter, test_basic_filter_detail)
class Filter(BaseCase):
    @parameterized.expand([(test_category_detail, test_basic_filter, test_basic_filter_detail)
    ])
    def test_set_filter(self, category2: str, basic_filter1: str, basic_filter2: str):
        try:
            self.open("https://kream.co.kr/")
            self.click('a:contains("SHOP")')
            self.wait_for_element("div.content-container")
            self.click('p.text-group span:contains("카테고리")')
            self.click('div.shop-filter-sections button:contains("더보기")')
            self.wait_for_element('div.shop_filter_section_bubble span:contains("%s")' % "기타 가구/리빙")
            self.click('button.filter_button.tint span.title:contains("%s")' % category2)
            if basic_filter1 in ["성별","혜택/할인"]:
                self.click('button.filter_button.tint span:contains("%s")' % basic_filter2)
            elif basic_filter1 == "색상":
                self.click('div.shop-filter-sections.color svg')
                self.click('div.filter-shortcut p:contains("%s")' % basic_filter2)
            elif basic_filter1 == "브랜드":
                self.click('div.shop-filter-sections.brand svg')
                self.click('div.filter_chip_group span:contains("%s")' % basic_filter2)
            elif basic_filter1 == "사이즈":
                self.click('div.shop-filter-sections.tag_id[size] svg')
                self.click('button.filter_button.tint span:contains("%s")' % basic_filter2)
            elif basic_filter1 == "가격대":
                self.click('div.shop-filter-sections.price svg')
                self.click('button.filter_button.tint span:contains("%s")' % basic_filter2)
            else:
                pass
            self.click('a.btn.full.solid')
            pause.pause_while()
            # self.click('li.menu span:contains("%s")' % test_category)
            # self.click('li.menu span:contains("%s")' % test_category_detail)
            # self.click('div.title_box span:contains("%s")' % test_basic_filter)
            # self.wait_for_element('li.menu a.menu_link span.link_txt')
            # self.click('li.menu p:contains("%s")' % test_category_detail)
            # self.click('button.sorting_title')
            # if data_filter != "추천순":
            #     self.click('li.sorting_item p:contains("%s")' % test_data_filter)
        except Exception as e:
            print(f"필터적용 실패: {e}")

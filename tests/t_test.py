from seleniumbase import BaseCase
from parameterized import parameterized
from src.utils.pause import pause_while

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
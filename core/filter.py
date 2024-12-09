from utils.data_manager import DataManager
from utils.pause import pause_while

class Filter:
    def __init__(self, sb):
        self.sb = sb

    def perform_filter(self, filters):

        try:
            self.sb.click('a:contains("SHOP")')
            self.sb.sleep(1)
            self.sb.wait_for_element("div.content-container")
            self.sb.click('p.text-group span:contains("카테고리")')
            ## 필터리셋시키기
            self.sb.click('div.shop-filter-sections.category.expanded span.collapse-icon')
            self.sb.click('div.shop-filter-sections.gender.expanded span.collapse-icon')
            self.sb.click('div.shop-filter-sections.benefits.expanded span.collapse-icon')
            ## 카테고리필터키기
            self.sb.click('div.shop-filter-sections.category span.collapse-icon')
            self.sb.click('div.shop-filter-sections button:contains("더보기")')

            ## 카테고리선택 -> 모두 선택 카테고리에서는 없음
            self.sb.click('button.filter_button.tint span:contains("%s")' % filters['category_detail'])
            self.sb.click('div.shop-filter-sections.category.expanded span.collapse-icon')

            ## 성별선택
            if filters['gender'] != "" and self.sb.is_element_present('div.shop-filter-sections.gender'):
                self.sb.click('div.shop-filter-sections.gender span.collapse-icon')
                if self.sb.is_element_visible('p.text-group span:contains("%s")' % filters['gender']):
                    self.sb.click('p.text-group span:contains("%s")' % filters['gender'])
                self.sb.click('div.shop-filter-sections.gender.expanded span.collapse-icon')
            
            ## 색상선택
            if filters['color'] != "" and self.sb.is_element_present('div.shop-filter-sections.color'):
                    self.sb.click('div.shop-filter-sections.color span.collapse-icon')
                    self.sb.click('div.shop-filter-sections.color p:contains("%s")' % filters['color'])
                    self.sb.click('div.shop-filter-sections.color.expanded span.collapse-icon')
            ## 혜택/할인 선택
            if filters['benefit'] != "" and self.sb.is_element_present('div.shop-filter-sections.benefits'):
                self.sb.click('div.shop-filter-sections.benefits span.collapse-icon')
                if filters['benefit_detail'] == "모두 선택":
                    self.sb.click("//p[contains(text(), '%s')]/following-sibling::button[@class='btn_multiple']" % filters['benefit'])
                else:
                    if self.sb.is_element_visible('div.shop-filter-sections.benefits span:contains("%s")' % filters['benefit_detail']):
                        self.sb.click('div.shop-filter-sections.benefits span:contains("%s")' % filters['benefit_detail'])
                self.sb.click('div.shop-filter-sections.benefits.expanded span.collapse-icon')


        except Exception as e:
            print(f"필터 실패: {e}")
    


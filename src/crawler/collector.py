
from src.utils.pause import pause_while

class Collector():
    def __init__(self, sb):
        self.sb = sb  # seleniumbase 인스턴스생성후 실행하기
    

    def perform_login(self, email, password):
        try:
            self.sb.open("https://kream.co.kr/")
            self.sb.click('a[href="/login"]')
            self.sb.type('input[type="email"]', email)
            self.sb.type('input[type="password"]', password)
            self.sb.click('button[type="submit"]')
        
        except Exception as e:
            print(f"로그인 실패: {e}")


    def perform_filter(self, filters):
        try:
            self.sb.click('a:contains("SHOP")')
            self.sb.sleep(1)
            self.sb.wait_for_element("div.content-container")
            self.sb.click('p.text-group span:contains("카테고리")')
            self.sb.click('div.shop-filter-sections.gender.expanded span.collapse-icon')
            self.sb.click('div.shop-filter-sections.benefits.expanded span.collapse-icon')
            ## 카테고리필터키기
            self.sb.click('div.shop-filter-sections button:contains("더보기")')
            ## 카테고리선택 -> 모두 선택 카테고리에서는 없음
            self.sb.hover('div.shop-filter-sections.category.expanded div.section_titles p:contains("%s")' % filters['category'])
            self.sb.click('button.filter_button.tint span:contains("%s")' % filters['category_detail'])
            self.sb.click('div.shop-filter-sections.category.expanded span.collapse-icon')
            self.sb.sleep(1)

            ## 성별선택
            if filters['gender'] != "" and self.sb.is_element_present('div.shop-filter-sections.gender'):
                self.sb.click('div.shop-filter-sections.gender span.collapse-icon')
                if self.sb.is_element_visible('p.text-group span:contains("%s")' % filters['gender']):
                    self.sb.click('p.text-group span:contains("%s")' % filters['gender'])
                self.sb.click('div.shop-filter-sections.gender.expanded span.collapse-icon')
                self.sb.sleep(1)
            
            ## 색상선택
            if filters['color'] != "" and self.sb.is_element_present('div.shop-filter-sections.color'):
                self.sb.click('div.shop-filter-sections.color span.collapse-icon')
                if self.sb.is_element_visible('div.shop-filter-sections.color p:contains("%s")' % filters['color']):
                    self.sb.click('div.shop-filter-sections.color p:contains("%s")' % filters['color'])
                self.sb.click('div.shop-filter-sections.color.expanded span.collapse-icon')
                self.sb.sleep(1)

            ## 혜택/할인 선택
            if filters['benefit'] != "" and self.sb.is_element_present('div.shop-filter-sections.benefits'):
                self.sb.click('div.shop-filter-sections.benefits span.collapse-icon')
                if filters['benefit_detail'] == "모두 선택":
                    self.sb.click("//p[contains(text(), '%s')]/following-sibling::button[@class='btn_multiple']" % filters['benefit'])
                else:
                    if self.sb.is_element_visible('div.shop-filter-sections.benefits span:contains("%s")' % filters['benefit_detail']):
                        self.sb.click('div.shop-filter-sections.benefits span:contains("%s")' % filters['benefit_detail'])
                self.sb.click('div.shop-filter-sections.benefits.expanded span.collapse-icon')
                self.sb.sleep(1)
            
            ## 브랜드선택
            if filters['brand'] != "" and self.sb.is_element_present('div.shop-filter-sections.brand'):
                self.sb.click('div.shop-filter-sections.brand span.collapse-icon')
                if self.sb.is_element_visible('div.filter-section-list.brand div.section_titles p.title:contains("%s")' % filters['brand']):
                    self.sb.hover('div.section_contents span:contains("%s")' % filters['brand_detail'])
                    self.sb.click('div.section_contents span:contains("%s")' % filters['brand_detail'])
                else:
                    pass
                self.sb.click('div.shop-filter-sections.brand.expanded span.collapse-icon')
                self.sb.sleep(1)

            ## 컬렉션 선택
            if filters['collection'] != "" and self.sb.is_element_present('div.shop-filter-sections.collection'):
                self.sb.click('div.shop-filter-sections.collection span.collapse-icon')
                if self.sb.is_element_visible('div.section_contents span:contains("%s")' % filters['collection']):
                    self.sb.hover_and_click('div.section_contents span:contains("%s")' % filters['collection'])
                else:
                    pass
                self.sb.click('div.shop-filter-sections.collection.expanded span.collapse-icon')
                self.sb.sleep(1)

            ## 사이즈 선택
            if filters['size'] != "" and self.sb.is_element_present('div.shop-filter-sections.tag_id\[size\]'):
                self.sb.click('div.shop-filter-sections.tag_id\[size\] span.collapse-icon')
                if self.sb.is_element_visible('div.filter-section-list.tag_id\[size\] div.section_titles p.title:contains("%s")' % filters['size']):
                    self.sb.click('div.section_contents span:contains("%s")' % filters['size_detail'])
                self.sb.click('div.shop-filter-sections.tag_id\[size\].expanded span.collapse-icon')  
                self.sb.sleep(1)

            ## 가격 선택
            if filters['price'] != "" and self.sb.is_element_present('div.shop-filter-sections.price'):
                self.sb.click('div.shop-filter-sections.price span.collapse-icon')
                self.sb.hover_and_click('div.shop-filter-sections.price div.vue-slider-rail', 'button.filter_button.tint span:contains("%s")' % filters['price'])
                self.sb.click('div.shop-filter-sections.price.expanded span.collapse-icon')
                self.sb.sleep(1)
            ## 필터적용
            self.sb.click('a.btn.full.solid')
            self.sb.sleep(1)
            
            ## sorting
            if filters['sorting'] == "인기순":
                pass
            else:
                self.sb.click('div.content-container button.sorting_title')
                self.sb.click('li.sorting_item p:contains("%s")' % filters['sorting'])

        except Exception as e:  
            print(f"필터 실패: {e}")
## 크롤링에서 자주사용하는 SeleniumBase 함수선언하기
from seleniumbase import BaseCase


class TestFunction(BaseCase):
    def setUp(self):
        super().setUp()
    
    def tearDown(self):
        super().tearDown()

    ## TODO:유닛테스트 작성후에 기능 추가하자!!
    ## open and type and submit
    def function(self, url, link_text, input_type, input_value, button_class_name, new_link_text):
        try:
            self.open(url)
            self.click('a:contains("%s")' % link_text)
            self.type('input[type="%s"]' % input_type, input_value)
            self.click(f'button.{button_class_name}')
            self.wait_for_element('a:contains("%s")' % new_link_text)
        except Exception as e:
            print(f"function 실패: {e}")
    ## open and scroll and condition click
    def function2(self, url, link_text, new_link_text, hover_text, conditon_class_name, click_text, condition_text, click_text2):
        try:
            self.open(url)
            self.click('a:contains("%s")' % link_text)
            self.wait_for_element('a:contains("%s")' % new_link_text)
            self.hover('p:contains("%s")' % hover_text)
            if self.is_element_present(f'div.{conditon_class_name}'):
                self.click(f'div.{click_text}')
                if self.is_element_visible(f'span:contains("%s")' % condition_text):
                    self.click(f'span:contains("%s")' % click_text2)
            
        except Exception as e:
            print(f"function2 실패: {e}")
    
    def function3(self):
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
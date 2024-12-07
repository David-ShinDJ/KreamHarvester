from utils.data_manager import DataManager
from utils.pause import pause_while

class Filter:
    def __init__(self, filters, sb):
        self.filters = filters
        self.sb = sb

    def perform_filter(self):
        try:
            self.sb.click('a:contains("SHOP")')
            self.sb.sleep(1)
            self.sb.wait_for_element("div.content-container")
            self.sb.click('p.text-group span:contains("카테고리")')
        except Exception as e:
            print(f"필터 실패: {e}")
    


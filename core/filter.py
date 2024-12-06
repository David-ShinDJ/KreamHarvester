from utils import *
from seleniumbase import SB


class Filter:
    def __init__(self, filters):
        self.filters = filters
    

    def select_category(self):
        
        input("카테고리 선택 완료")
    def perform_filter(self):
        with SB() as sb:
            sb.sleep(1)
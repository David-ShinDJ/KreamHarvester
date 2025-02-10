from seleniumbase import BaseCase
from ..models.product import Product, ProductInfo

class KreamCollector(BaseCase):
    def __init__(self, headless=False):
        super().__init__()
        self.headless = headless
    
    def collect_product(self, keyword, count):
        # 크롤링 로직 구현
        pass 
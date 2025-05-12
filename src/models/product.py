
class Product:
    def __init__(self, 
                 name: str = None,                    # 제품_이름
                 url: str = None,                      # 제품_URL
                 product_id: str = None,               # 제품_id
                 category: str = None,                 # 제품_카테고리
                 brand: str = None,                    # 브랜드
                 model_number: str = None,             # 제품_품번
                 immediate_buy_price: int = None,      # 즉시구매가격
                 storage_sell_price: int = None,       # 보관판매가격
                 immediate_sell_price: int = None,     # 즉시판매가격
                 total_sales: int = None,              # 총판매량
                 storage_latest_date: str = None,      # 보판_최근체결날짜
                 storage_latest_price: int = None,     # 보판_최근체결금액
                 storage_week_sales: int = None,       # 보판_최근7일체결량
                 total_latest_date: str = None  ,        # 전체_최근체결날짜
                 total_latest_price: int = None ,       # 전체_최근체결금액
                 total_week_sales: int = None,         # 전체_최근7일체결량
                 option_name: str = None):      # 옵션명
        # 제품 식별 정보
        self.name = name
        self.url = url
        self.product_id = product_id
        self.category = category
        self.brand = brand
        self.model_number = model_number
        
        # 가격 정보
        self.immediate_buy_price = immediate_buy_price
        self.storage_sell_price = storage_sell_price
        self.immediate_sell_price = immediate_sell_price
        
        # 판매 정보
        self.total_sales = total_sales
        self.storage_latest_date = storage_latest_date
        self.storage_latest_price = storage_latest_price
        self.storage_week_sales = storage_week_sales
        self.total_latest_date = total_latest_date
        self.total_latest_price = total_latest_price
        self.total_week_sales = total_week_sales
        
        # 옵션 정보
        self.option_name = option_name
        
        # 계산된 속성
        if self.storage_sell_price and self.immediate_buy_price:
            self.storage_margin = self.storage_sell_price - self.immediate_buy_price
            self.immediate_margin = self.immediate_sell_price - self.immediate_buy_price
            self.storage_margin_rate = format(self.storage_margin / self.storage_sell_price, ".2f")
            self.immediate_margin_rate = format(self.immediate_margin / self.immediate_sell_price, ".2f")
    
    def __str__(self):
        return (f"Product(name='{self.name}', "
                f"url='{self.url}', "
                f"product_id='{self.product_id}', "
                f"category='{self.category}', "
                f"brand='{self.brand}', "
                f"model_number='{self.model_number}', "
                f"immediate_buy_price={self.immediate_buy_price}, "
                f"storage_sell_price={self.storage_sell_price}, "
                f"immediate_sell_price={self.immediate_sell_price}, "
                f"total_sales={self.total_sales}, "
                f"storage_margin={self.storage_margin}, "
                f"immediate_margin={self.immediate_margin}, "
                f"storage_margin_rate={self.storage_margin_rate}, "
                f"immediate_margin_rate={self.immediate_margin_rate}, "
                f"option_name='{self.option_name}')")
    
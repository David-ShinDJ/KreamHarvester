class Product:
    def __init__(self, 
            index: int = None,                    # 인덱스
            url: str = None,                      # url
            review_point: str = None,             # 별점
            size: str = None,                     # 사이즈
            immediate_buy_price: int = None,      # 즉시구매가격
            immediate_sell_price: int = None,     # 즉시판매가격
            early_delivery_price: int = None,     # 빠른배송가격
            early_delivery_nf_price: int = None,  # 빠른배송95가격
            recent_trade_price: int = None,       # 최근거래가
            release_price: int = None,            # 발매가
            model_number: str = None,             # 모델번호   
            release_date: str = None,             # 출시일
            representative_color: str = None,     # 대표색상
            recent_7_day_sales_5: int = None,      # 최근 7일 체결량 top5
            sales_bid_5: int = None,              # 판매입찰 top5
    ):
        self.index = index
        self.url = url
        self.review_point = review_point
        self.size = size
        self.immediate_buy_price = immediate_buy_price
        self.immediate_sell_price = immediate_sell_price
        self.early_delivery_price = early_delivery_price
        self.early_delivery_nf_price = early_delivery_nf_price
        self.recent_trade_price = recent_trade_price
        self.release_price = release_price
        self.model_number = model_number
        self.release_date = release_date
        self.representative_color = representative_color
        self.recent_7_day_sales_5 = recent_7_day_sales_5
        self.sales_bid_5 = sales_bid_5

    @property
    def storage_sales_margin(self) -> int:
        """빠른배송 판매 마진"""
        if self.early_delivery_price and self.immediate_buy_price:
            return self.early_delivery_price - self.immediate_buy_price
        return None

    @property
    def storage_sales_margin_rate(self) -> float:
        """빠른배송 판매 마진률"""
        if self.early_delivery_price and self.immediate_buy_price:
            return round((self.early_delivery_price - self.immediate_buy_price) / self.early_delivery_price, 2)
        return None
    
    @property
    def storage_nf_sales_margin(self) -> int:
        """빠른배송 95 판매 마진"""
        if self.early_delivery_nf_price and self.immediate_buy_price:
            return self.early_delivery_nf_price - self.immediate_buy_price
        return None
    
    @property
    def storage_nf_sales_margin_rate(self) -> float:
        """빠른배송 95 판매 마진률"""
        if self.early_delivery_nf_price and self.immediate_buy_price:
            return round((self.early_delivery_nf_price - self.immediate_buy_price) / self.early_delivery_nf_price, 2)
        return None
    
    
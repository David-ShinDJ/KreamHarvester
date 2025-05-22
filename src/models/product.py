class Product:
    def __init__(self, 
            index: int,                           # 인덱스
            trade_volume: str = None,             # 거래량
            brand : str = None,                  # 브랜드
            name : str = None,                   # 상품명
            ko_name : str = None,                # 한글 상품명
            lowest_immediate_buy_price : int = None, # 최저 즉시 구매가# 최고 즉시 구매가
            likes : int = None,                  # 관심
            reviews : int = None,                # 리뷰
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
        self.trade_volume = trade_volume
        self.brand = brand
        self.name = name
        self.ko_name = ko_name
        self.lowest_immediate_buy_price = lowest_immediate_buy_price
        self.likes = likes
        self.reviews = reviews
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
    
    def __str__(self):
        return f"""Product(
            index: {self.index},
            trade_volume: {self.trade_volume},
            brand: {self.brand},
            name: {self.name},
            ko_name: {self.ko_name},
            lowest_immediate_buy_price: {self.lowest_immediate_buy_price},
            likes: {self.likes},
            reviews: {self.reviews},
            url: {self.url},
            review_point: {self.review_point},
            size: {self.size},
            immediate_buy_price: {self.immediate_buy_price},
            immediate_sell_price: {self.immediate_sell_price},
            early_delivery_price: {self.early_delivery_price},
            early_delivery_nf_price: {self.early_delivery_nf_price},
            recent_trade_price: {self.recent_trade_price},
            release_price: {self.release_price},
            model_number: {self.model_number},
            release_date: {self.release_date},
            representative_color: {self.representative_color},
            recent_7_day_sales_5: {self.recent_7_day_sales_5},
            sales_bid_5: {self.sales_bid_5},
            storage_sales_margin: {self.storage_sales_margin},
            storage_sales_margin_rate: {self.storage_sales_margin_rate},
            storage_nf_sales_margin: {self.storage_nf_sales_margin},
            storage_nf_sales_margin_rate: {self.storage_nf_sales_margin_rate}
        )"""


## 썸네일 사용 X 
class Thumbnail:
    def __init__(
            self, index : int,
            trade_volume : str = None, # 거래량
            brand : str = None, # 브랜드
            name : str = None, # 상품명
            lowest_immediate_buy_price : int = None, # 최저 즉시 구매가# 최고 즉시 구매가
            likes : int = None, # 관심
            reviews : int = None, # 리뷰
        ):
        self.index = index
        self.trade_volume = trade_volume
        self.brand = brand
        self.name = name
        self.lowest_immediate_buy_price = lowest_immediate_buy_price
        self.likes = likes
        self.reviews = reviews

    def __str__(self):
        return f"index: {self.index}, brand: {self.brand}, name: {self.name}, lowest_immediate_buy_price: {self.lowest_immediate_buy_price}, likes: {self.likes}, reviews: {self.reviews}"



    # @parameterized.expand([
    #     1
    # ])
    # def test_extract_thumbnail_info(self, index: int,):
    #     """ 제품 검색 및 클릭 """
    #     try:
    #         self.open("https://kream.co.kr/search")
    #         thumbnail_info = Thumbnail(index=index)
    #         text = self.get_text(f'div[data-result-index="{index}"]')
    #         text_list = text.split("\n")# 디버깅용 출력
    #         thumbnail_info.trade_volume = text_list[0].replace("거래 ", "")  # "거래 1.3만" -> "1.3만"
    #         thumbnail_info.brand = text_list[1]  # "Asics"
    #         thumbnail_info.name = text_list[3]   # "아식스 젤 소노마 15-50 블랙"
    #         thumbnail_info.lowest_immediate_buy_price = text_list[5].replace("원", "").replace(",", "")  # "145,000원" -> "145000"
    #         thumbnail_info.likes = text_list[7]  # "3.2만"
    #         thumbnail_info.reviews = text_list[8]  # "236"
    #     except Exception as e:
    #         print(f"제품 검색 테스트 실패: {e}")
    #     finally:
    #         print(f"포인터 정보: {thumbnail_info}")
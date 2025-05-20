    
    ## TODO: 썸네일데이터에서 추출할수있는값 거래량 브랜드, 상품명, 가격, 관심, 리뷰 

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
    
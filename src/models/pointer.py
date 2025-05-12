
class Pointer:
    def __init__(
            self, index : int,
            product_trade_volume : str = None,
            product_brand : str = None,
            product_name : str = None,
            product_immediate_buy_price_average : str = None,
            product_likes : int = None,
            product_reviews : int = None,
        ):
        self.index = index
        self.product_trade_volume = product_trade_volume
        self.product_brand = product_brand
        self.product_name = product_name
        self.product_immediate_buy_price_average = product_immediate_buy_price_average
        self.product_likes = product_likes
        self.product_reviews = product_reviews

    def __str__(self):
        return f"index: {self.index}, brand: {self.product_brand}, name: {self.product_name}, immediate_buy_price_average: {self.product_immediate_buy_price_average}, likes: {self.product_likes}, reviews: {self.product_reviews}"
    
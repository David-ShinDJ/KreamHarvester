class Filter:
    def __init__(self,
                 category1: str = None,          # 카테고리1
                 category2: str = None,          # 카테고리2
                 keyword: str = None,            # 검색어
                 sort_by: str = None,            # 정렬기준
                 min_margin: float = None,       # 최소마진
                 exclude_storage: bool = False,  # 보관판매불감제품_제외
                 exclude_release_above: bool = False,  # 발매가 > 즉시판매가 제외
                 exclude_no_release: bool = False,     # 발매가없는제품_제외
                 min_total_sales: int = None,    # 총판매량_최소
                 min_period_sales: int = None,   # 기간체결량_최소
                 min_immediate_price: int = None,  # 즉구가_최소
                 max_immediate_price: int = None,  # 즉구가_최대
                 size_options: str = None):       # 옵션필터링 (콤마로 구분)
        
        # 카테고리 및 검색 설정
        self.category1 = category1
        self.category2 = category2
        self.keyword = keyword
        self.sort_by = sort_by
        
        # 마진 설정
        self.min_margin = min_margin
        
        # 제외 조건
        self.exclude_storage = exclude_storage
        self.exclude_release_above = exclude_release_above
        self.exclude_no_release = exclude_no_release
        
        # 판매량 설정
        self.min_total_sales = min_total_sales
        self.min_period_sales = min_period_sales
        
        # 가격 범위 설정
        self.min_immediate_price = min_immediate_price
        self.max_immediate_price = max_immediate_price
        
        # 사이즈 옵션 설정
        self.size_options = size_options.split(',') if size_options else []
    
    def is_valid_product(self, product) -> bool:
        """제품이 필터 조건을 만족하는지 확인"""
        try:
            # 마진 계산
            storage_margin = product.storage_sell_price - product.immediate_buy_price
            immediate_margin = product.immediate_sell_price - product.immediate_buy_price
            
            # 마진 범위 체크
            if self.min_margin is not None and storage_margin < self.min_margin:
                return False
            
            # 제외 조건 체크
            if self.exclude_storage and product.storage_week_sales == 0:
                return False
            if self.exclude_release_above and product.release_price > product.immediate_sell_price:
                return False
            if self.exclude_no_release and not product.release_price:
                return False
            
            # 판매량 체크
            if self.min_total_sales is not None and product.total_sales < self.min_total_sales:
                return False
            if self.min_period_sales is not None and product.total_week_sales < self.min_period_sales:
                return False
            
            # 가격 범위 체크
            if self.min_immediate_price is not None and product.immediate_buy_price < self.min_immediate_price:
                return False
            
            # 사이즈 옵션 체크
            if self.size_options and product.option_name:
                product_sizes = [size.strip() for size in product.option_name.split(',')]
                if not any(size in product_sizes for size in self.size_options):
                    return False
            
            return True
            
        except Exception as e:
            print(f"필터 검증 중 오류 발생: {e}")
            return False
    
    def __str__(self):
        return (f"Filter(category1='{self.category1}', "
                f"category2='{self.category2}', "
                f"keyword='{self.keyword}', "
                f"sort_by='{self.sort_by}', "
                f"min_margin={self.min_margin}, "
                f"exclude_storage={self.exclude_storage}, "
                f"exclude_release_above={self.exclude_release_above}, "
                f"exclude_no_release={self.exclude_no_release}, "
                f"min_total_sales={self.min_total_sales}, "
                f"min_period_sales={self.min_period_sales}, "
                f"min_immediate_price={self.min_immediate_price}, "
                f"max_immediate_price={self.max_immediate_price}, "
                f"size_options={self.size_options})")
    
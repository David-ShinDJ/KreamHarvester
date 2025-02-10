class ProductInfo:
    def __init__(self, rtp, rpc, rp, mn, rd, rc):
        self.rtp = rtp  # 최근거래가
        self.rpc = rpc  # 최근가격변동
        self.rp = rp    # 발매가
        self.mn = mn    # 모델번호
        self.rd = rd    # 출시일
        self.rc = rc    # 대표색상

    def __str__(self):
        return f"ProductInfo(rtp={self.rtp}, rpc={self.rpc}, rp={self.rp}, mn={self.mn}, rd={self.rd}, rc={self.rc})"
    

class Product:
    def __init__(self, name:str, url:str, option:str | None, ipp:int, ssp:int, info:ProductInfo):
        self.name = name
        self.url = url
        self.option = option  # option 변수 할당이 누락되어 있었음
        self.ipp = ipp
        self.ssp = ssp
        self.m = self.ssp - self.ipp
        self.mr = format((self.ssp - self.ipp) / self.ssp, ".2f")  # 수식 괄호 수정
        self.info = info
        
    def __str__(self):
        return f"Product(name={self.name}, url={self.url}, option={self.option}, ipp={self.ipp}, ssp={self.ssp}, m={self.m}, mr={self.mr}, info={self.info})"
    
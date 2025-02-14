from src.crawler.collector import Collector
from seleniumbase import SB
from src.utils.pause import pause_while
# with 구문으로 SB 인스턴스 생성
        #    ("아우터", "패딩", "남성", "블랙", "혜택", "모두 선택", "N", "Nike", "Luxury", "의류", "XL", "30-50만원", "남성 인기순"),
        #     ("신발", "스니커즈", "여성", "아이보리", "할인율", "30% 이하", "T", "Tabi", "Contemporary", "신발", "240", "20만원대", "여성 인기순"),
# email, password = input_login()
email = "ehdwnsqkqhek@naver.com"
password = "Tls1169511!"
filters = {
    "category": "아우터",
    "category_detail": "패딩",
    "gender": "남성",
    "color": "블랙",
    "benefit": "혜택",
    "benefit_detail": "모두 선택",
    "brand": "N",
    "brand_detail": "Nike",
    "collection": "Luxury",
    "size": "의류",
    "size_detail": "XL",
    "price": "30-50만원",
    "sorting": "남성 인기순",
}
filters2 = {
    "category": "신발",
    "category_detail": "스니커즈",
    "gender": "여성",
    "color": "아이보리",
    "benefit": "할인율",
    "benefit_detail": "30% 이하",
    "brand": "T",
    "brand_detail": "Tabi",
    "collection": "Contemporary",
    "size": "신발",
    "size_detail": "240",
    "price": "20만원대",
    "sorting": "여성 인기순",
}

with SB() as sb:
    collector = Collector(sb=sb)
    collector.perform_login(email=email, password=password)
    collector.perform_filter(filters=filters2)
    # login_module = Login(sb=sb)
    # filter_module = Filter(sb=sb)
    # # login 기능
    # login_module.perform_login(email=email, password=password)
    # sb.sleep(3)

print("메인 실행")
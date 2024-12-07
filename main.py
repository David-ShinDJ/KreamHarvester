import time
from seleniumbase import SB
from selenium.webdriver.common.by import By
from utils.sele import SeleniumManager
from utils.data_manager import DataManager
from core.filter import Filter
from core.login import Login
from utils.pause import pause_while
# with 구문으로 SB 인스턴스 생성
with SB() as sb:
    login_module = Login(email="ehdwnsqkqhek@naver.com", password="Tls1169511!", sb=sb)
    filter_module = Filter(filters={}, sb=sb)
    # login 기능
    login_module.perform_login()
    sb.sleep(3)
    # Filter 기능
    filter_module.perform_filter()
    
    pause_while()

##data_manager 생성
data_manager = DataManager()
## filter 선택하기 -> 원하는 필터 선택 없는경우 "" 입력 -> ## TODO: 복수필터선택 및 모두선택 기능 추가해야함
def select_filter(data_manager):
        filters = {
            "category": "",
            "category_detail": "",
            "gender": "",
            "color": "",
            "benefit": "",
            "benefit_detail": "",
            "brand": "",
            "collection": "",
            "size": "",
            "size_detail": "",
            "price": "",
            "sorting": "",
        }
        category = input(f"{data_manager.json_to_dictionary('category').keys()} 중 하나를 입력하세요 : ")
        filters["category"] = category
        category_detail = input(f"{data_manager.json_to_dictionary('category')[category]} 중 하나를 입력하세요 : ")
        filters["category_detail"] = category_detail
        gender = input(f"{data_manager.json_to_list('gender')} 중 하나를 입력하세요 : ")
        filters["gender"] = gender
        color = input(f"{data_manager.json_to_list('color')} 중 하나를 입력하세요 : ")
        filters["color"] = color
        benefit = input(f"{data_manager.json_to_dictionary('benefit').keys()} 중 하나를 입력하세요 : ")
        filters["benefit"] = benefit
        benefit_detail = input(f"{data_manager.json_to_dictionary('benefit')[benefit]} 중 하나를 입력하세요 : ")
        filters["benefit_detail"] = benefit_detail
        brand = input(f"{data_manager.json_to_list('brand')} 중 하나를 입력하세요 : ")
        filters["brand"] = brand
        collection = input(f"{data_manager.json_to_list('collection')} 중 하나를 입력하세요 : ")
        filters["collection"] = collection
        size = input(f"{data_manager.json_to_dictionary('size').keys()} 중 하나를 입력하세요 : ")
        filters["size"] = size
        size_detail = input(f"{data_manager.json_to_dictionary('size')[size]} 중 하나를 입력하세요 : ")
        filters["size_detail"] = size_detail
        price = input(f"{data_manager.json_to_list('price')} 중 하나를 입력하세요 : ")
        filters["price"] = price
        sorting = input(f"{data_manager.json_to_list('sorting')} 중 하나를 입력하세요 : ")
        filters["sorting"] = sorting
        return filters

# filters = select_filter(data_manager)
# print(filters.keys(), filters.values())


# # Filter 기능
# Selector Category

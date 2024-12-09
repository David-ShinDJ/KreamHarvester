import time
from seleniumbase import SB
from selenium.webdriver.common.by import By
from utils.data_manager import DataManager
from utils.sele import SeleniumManager
from core.filter import Filter
from core.login import Login
from utils.pause import pause_while
from utils.select_filter import select_filter
# with 구문으로 SB 인스턴스 생성
# filters = select_filter()
# with SB() as sb:
#     login_module = Login(email="ehdwnsqkqhek@naver.com", password="Tls1169511!", sb=sb)
#     filter_module = Filter(filters={}, sb=sb)
#     # login 기능
#     login_module.perform_login()
#     sb.sleep(3)
#     # Filter 기능
#     filter_module.perform_filter(filters=filters)
#     pause_while()

##data_manager 생성
## filter 선택하기 -> 원하는 필터 선택 없는경우 "" 입력 -> ## TODO: 복수필터선택 및 모두선택 기능 추가해야함

data_manager_module = DataManager()
data_manager_module.get_filters_data()
data_manager_module.data_to_json()





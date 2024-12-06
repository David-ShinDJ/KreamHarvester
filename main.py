import time
from selenium.webdriver.common.by import By
from utils.sele import SeleniumManager
from utils.data_manager import DataManager
# # login 기능
# login_module = login.Login(email="ehdwnsqkqhek@naver.com", password="Tls1169511!")
# login_module.perform_login()


sele_module = SeleniumManager()
sele_module.open_url("https://kream.co.kr/search")
# Filter_Data : category 생성
sele_module.click_element(selector="//span[@class='title' and contains(text(), '카테고리')]", by=By.XPATH)
sele_module.click_element('div.view-more button[type=button]')
text_element = sele_module.get_text_element("div.shop-filter-sections-wrap div.shop-filter-sections.active.category.expanded")
data_manager_module = DataManager()
data_manager_module.element_to_text(text_element, "category")
category_dictionary = data_manager_module.data_to_dictionary('category',
                                                      ["아우터", "상의", "신발", "하의", "가방", "지갑", "시계", "패션잡화", "컬렉터블", "뷰티",
                                                       "테크", "캠핑", "가구/리빙"], case="filter", detail="category")
data_manager_module.dictionary_to_json(category_dictionary, 'category')
# Sorting Data & json 생성
sele_module.open_url("https://kream.co.kr/search")
sele_module.click_element(selector='div.content-container button.sorting_title')
text_element = sele_module.get_text_element('ul.sorting_list')
data_manager_module.element_to_text(text_element, "sorting")
data_manager_module.list_to_json(data_manager_module.data_to_list('sorting'), 'sorting')

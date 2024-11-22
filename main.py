import time
from selenium.webdriver.common.by import By
import utils.sele as sele_module
from utils.data_manager import DataManager
# # login 기능
# login_module = login.Login(email="ehdwnsqkqhek@naver.com", password="Tls1169511!")
# login_module.perform_login()


module = sele_module.SeleniumManager()
module.open_url("https://kream.co.kr/search")
# Filter_Data : category 생성
module.click_element(selector="//span[@class='title' and contains(text(), '카테고리')]", by=By.XPATH)
module.click_element('div.view-more button[type=button]')
module.save_text("div.shop-filter-sections-wrap div.shop-filter-sections.active.category.expanded",
                          filename="category")
module2 = DataManager()
category_dic = module2.data_to_dictionary('category',
                                                      ["아우터", "상의", "신발", "하의", "가방", "지갑", "시계", "패션잡화", "컬렉터블", "뷰티",
                                                       "테크", "캠핑", "가구/리빙"], case="filter")
module2.dictionary_to_json(category_dic, 'category')



import os, sys



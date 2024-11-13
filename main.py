import time

from core import *
from utils import *
from selenium.webdriver.common.by import By

# # login 기능
# login_module = login.Login(email="ehdwnsqkqhek@naver.com", password="Tls1169511!")
# login_module.perform_login()
#
# # pages : html 생성
# html_gen = bs4.SoupManager(url="https://kream.co.kr/search", page_name="search")
# html_gen.make_html()


## refs : tag_text.txt 생성
html_text_module = sele.SeleniumManager()
html_text_module.open_url("https://kream.co.kr/search")
# print(html_text_module.get_elements_num(selector='//span[@class="title" and text()="카테고리"]', by=By.XPATH))
html_text_module.click_element(selector="//span[@class='title' and contains(text(), '카테고리')]", by=By.XPATH)
# html_text_module.click_tag(selector='//span[@class="title" and text()="카테고리"]', by=By.XPATH)
html_text_module.click_element('div.view-more button[type=button]')
html_text_module.save_text("div.shop-filter-sections-wrap div.shop-filter-sections.active.category.expanded", filename="category")
# html_text_module.current_url()
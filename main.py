from core import *
from utils import *

# test = login.Login(email="ehdwnsqkqhek@naver.com", password="Tls1169511!")
# test.perform_login()


html_gen = bs4_html.SoupHtmlGenerator(url="https://kream.co.kr/search", page_name="search")
html_gen.make_html()



import requests
from bs4 import BeautifulSoup

class SoupManager:
    ## URL 넣으면 해당 페이지 index.html 생성
    def __init__(self, url, page_name):
        self.url = url
        self.response = requests.get(self.url)
        self.html_doc = self.response.text
        self.soup = BeautifulSoup(self.html_doc,'html.parser')
        self.page_name = page_name

    def _get_body(self):
        body_tag = self.soup.find("body")
        return body_tag

    def make_html(self):
        string_body = str(self._get_body())
        with open(f"/Users/david/Codings/PycharmProjects/KreamHarvester/pages/{self.page_name}.html", 'w') as f:
            f.write(string_body)
            f.close()
        print(f"{self.page_name} Page 생성완료")

# pages : html 생성
if __name__ == "__main__":
    html_generator = SoupManager(url="https://kream.co.kr/search", page_name="search")
    html_generator.make_html()
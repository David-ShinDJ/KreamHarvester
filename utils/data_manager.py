import json
from selenium.webdriver.common.by import By
from utils.sele import SeleniumManager
import sys

class DataManager:
    def __init__(self):
        script_path = sys.path[0]
        self.data_path = script_path + "/datas/"
        self.json_path = script_path + "/constants/"

    def element_to_text(self, element, text_file_name):
        self._write_data(element, text_file_name)


    def _read_data(self, text_file_name):
        with open(self.data_path + f"{text_file_name}.txt", 'r') as f:
            data = f.read()
            f.close()
        return data
    def _write_data(self, data, text_file_name):
        with open(self.data_path + f"{text_file_name}.txt", 'w') as f:
            f.write(data)
            f.close()
        print(f"{text_file_name}.txt 생성완료")

    def _read_json(self, json_file_name, data_type="list"):
        with open(self.json_path + f"{json_file_name}.json", 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            json_file.close()
        return data

    def _write_json(self, data, json_file_name):
        with open(self.json_path + f"{json_file_name}.json", "w", encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False)
            json_file.close()
        print(f"{json_file_name}.json 생성완료")

    def data_to_list(self, text_file_name: str, case=None):
        if case == "filter":
            data = self._read_data(text_file_name=text_file_name)
            data_list = data.splitlines()
            data_list = data_list[1:]
            return data_list
        else:
            data = self._read_data(text_file_name=text_file_name)
            data_list = data.splitlines()
            return data_list

    ## category-filter 케이스 경우 모두 선택 제외
    def data_to_dictionary(self, text_file_name: str, slicing_words, case=None, detail=None):
        if case == "filter":
            data = self._read_data(text_file_name=text_file_name)
            data_list = data.splitlines()
            if detail == "category":
                data_list = [category for category in data_list if category != "모두 선택"]
            data_list = data_list[1:]
            data_dictionary: dict[str, list[str]] = {}
            for i, word in enumerate(slicing_words):
                start_index = data_list.index(word) + 1  # 현재 word의 시작 위치

                # 다음 단어가 있는 경우, 해당 단어의 인덱스를 찾음
                if i + 1 < len(slicing_words):
                    next_word = slicing_words[i + 1]
                    end_index = data_list.index(next_word)  # 다음 단어의 시작 위치
                else:
                    # 마지막 단어라면 끝까지 슬라이싱
                    end_index = len(data_list)
                    # 슬라이싱 결과를 사전에 저장
                data_dictionary[word] = data_list[start_index:end_index]

            return data_dictionary
        else:
            data = self._read_data(text_file_name=text_file_name)
            data_list = data.splitlines()
            data_dictionary: dict[str, list[str]] = {}
            for i, word in enumerate(slicing_words):
                start_index = data_list.index(word) + 1  # 현재 word의 시작 위치

                # 다음 단어가 있는 경우, 해당 단어의 인덱스를 찾음
                if i + 1 < len(slicing_words):
                    next_word = slicing_words[i + 1]
                    end_index = data_list.index(next_word)  # 다음 단어의 시작 위치
                else:
                    # 마지막 단어라면 끝까지 슬라이싱
                    end_index = len(data_list)
                    # 슬라이싱 결과를 사전에 저장
                data_dictionary[word] = data_list[start_index:end_index]

            return data_dictionary

    def list_to_json(self, my_list, json_file_name):
        return self._write_json(my_list, json_file_name)

    def json_to_list(self, json_file_name):
        return self._read_json(json_file_name)

    def dictionary_to_json(self, my_dictionary, json_file_name):
        return self._write_json(my_dictionary, json_file_name)

    def json_to_dictionary(self, json_file_name):
        return self._read_json(json_file_name, "dictionary")



if __name__ == "__main__":
    print("Filter Data 크롤링코드 실행")
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
    ## data : kream filter html json 저장하기
    selenium_module = SeleniumManager()
    selenium_module.open_url("https://kream.co.kr/search")
    # Filter_Data : category 생성
    selenium_module.click_element(selector="//span[@class='title' and contains(text(), '카테고리')]", by=By.XPATH)
    selenium_module.click_element('div.view-more button[type=button]')
    selenium_module.save_text("div.shop-filter-sections-wrap div.shop-filter-sections.active.category.expanded", filename="category")
    data_manager = DataManager()
    category_dictionary = data_manager.data_to_dictionary('category', ["아우터", "상의", "신발", "하의", "가방", "지갑", "시계", "패션잡화", "컬렉터블", "뷰티", "테크", "캠핑", "가구/리빙"])
    data_manager.dictionary_to_json(category_dictionary, 'category')
    # Filter_Data : Color 생성
    selenium_module.click_element(selector="//span[@class='title' and contains(text(), '가격대')]", by=By.XPATH)
    selenium_module.click_element(selector='div.shop-filter-sections.color span.collapse-icon')
    selenium_module.save_text("div.shop-filter-sections-wrap div.shop-filter-sections.color.expanded", filename="color")
    color_list = data_manager.data_to_list('color')
    data_manager.dictionary_to_json(color_list,'color')

    # Filter_Data : brand 생성
    selenium_module.click_element(selector="//span[@class='title' and contains(text(), '혜택/할인')]", by=By.XPATH)
    selenium_module.click_element(selector="div.shop-filter-sections.category.expanded span.collapse-icon")
    selenium_module.click_element(selector="div.shop-filter-sections.gender.expanded span.collapse-icon")
    selenium_module.click_element(selector="div.shop-filter-sections.benefits.expanded span.collapse-icon")
    selenium_module.click_element(selector='div.shop-filter-sections.brand span.collapse-icon')
    selenium_module.save_text("div.shop-filter-sections-wrap div.shop-filter-sections.brand.expanded", filename="brand")
    brand_list = data_manager.data_to_list('brand')
    data_manager.list_to_json(brand_list,'brand')

    # Filter_Data : collection 생성
    selenium_module.click_element(selector="//span[@class='title' and contains(text(), '혜택/할인')]", by=By.XPATH)
    selenium_module.click_element(selector="div.shop-filter-sections.category.expanded span.collapse-icon")
    selenium_module.click_element(selector="div.shop-filter-sections.gender.expanded span.collapse-icon")
    selenium_module.click_element(selector="div.shop-filter-sections.benefits.expanded span.collapse-icon")
    selenium_module.click_element(selector='div.shop-filter-sections.collection span.collapse-icon')
    selenium_module.save_text("div.shop-filter-sections-wrap div.shop-filter-sections.collection.expanded", filename="collection")
    collection_list = data_manager.data_to_list('collection')
    data_manager.list_to_json(collection_list,'collection')

    # Filter_Data : size 생성
    selenium_module.click_element(selector="//span[@class='title' and contains(text(), '혜택/할인')]", by=By.XPATH)
    selenium_module.click_element(selector="div.shop-filter-sections.category.expanded span.collapse-icon")
    selenium_module.click_element(selector="div.shop-filter-sections.gender.expanded span.collapse-icon")
    selenium_module.click_element(selector="div.shop-filter-sections.benefits.expanded span.collapse-icon")
    selenium_module.click_element(selector='div.shop-filter-sections.tag_id\[size\] span.collapse-icon')
    selenium_module.save_text("div.shop-filter-sections-wrap div.shop-filter-sections.tag_id\[size\].expanded", filename="size")
    size_dictionary = data_manager.data_to_dictionary('size', ["신발", "의류"])
    data_manager.list_to_json(size_dictionary,'size')
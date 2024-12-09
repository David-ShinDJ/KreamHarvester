import json
from selenium.webdriver.common.by import By
import sys
import os
import time
# 프로젝트 루트 디렉토리를 Python 경로에 추가
from utils.sele import SeleniumManager

class DataManager:
    def __init__(self):
        project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.data_path = project_path + "/datas/"
        self.json_path = project_path + "/constants/"
        self.sele_manager = SeleniumManager()

    def text_to_data(self, text, text_file_name):
        # 텍스트 데이터를 줄바꿈 문자를 기준으로 분리합니다.
        items = text.splitlines()

        # 중복을 제거하면서 순서를 유지합니다.
        unique_items = dict.fromkeys(items)

        # 줄바꿈 문자로 연결하여 새로운 텍스트를 만듭니다.
        new_text = '\n'.join(unique_items)  # 마침표와 공백으로 문장 연결

        # 4. 파일에 쓰기
        if text_file_name == "benefit":
            self._write_data(text, text_file_name) 
        elif text_file_name == "price":
            lines = text.splitlines()  # 텍스트를 줄 단위로 분리
            lines = lines[:-2]  # 마지막 두 줄 제거
            new_text = "\n".join(lines)
            self._write_data(new_text, text_file_name) 
        else:
            self._write_data(new_text, text_file_name) 


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
        elif case == "benefit" or case == "size":
            data = self._read_data(text_file_name=text_file_name)
            data_list = data.splitlines()
            data_dictionary: dict[str, list[str]] = {}
            for i, word in enumerate(slicing_words):
                start_index = data_list.index(word) + 1 # 현재 word의 시작 위치
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
            data_dictionary[slicing_words[0]] = data_list[1:]
            return data_dictionary
    def list_to_json(self, my_list, json_file_name):
        return self._write_json(my_list, json_file_name)

    def json_to_list(self, json_file_name):
        return self._read_json(json_file_name)

    def dictionary_to_json(self, my_dictionary, json_file_name):
        return self._write_json(my_dictionary, json_file_name)

    def json_to_dictionary(self, json_file_name):
        return self._read_json(json_file_name, "dictionary")

    def get_filters_data(self):

        self.sele_manager.open_url("https://kream.co.kr/search")
        ## sorting
        self.sele_manager.click_element(selector='div.content-container button.sorting_title')
        text_element = self.sele_manager.get_text('ul.sorting_list')
        self.text_to_data(text_element, "sorting")
        self.sele_manager.click_element(selector='div.content-container button.sorting_title')

        ## modal category gender benefit 열려있는상태
        self.sele_manager.click_element(selector="//span[@class='title' and contains(text(), '카테고리')]", by=By.XPATH)

        ## category
        self.sele_manager.click_element('div.view-more button[type=button]')
        text_element = self.sele_manager.get_text("div.shop-filter-sections-wrap div.shop-filter-sections.active.category.expanded")
        self.sele_manager.click_element('div.shop-filter-sections.category.expanded span.collapse-icon')
        self.text_to_data(text_element, "category")
        
        ## gender
        text_element = self.sele_manager.get_text("div.shop-filter-sections-wrap div.shop-filter-sections.gender.expanded")
        self.sele_manager.click_element('div.shop-filter-sections.gender.expanded span.collapse-icon')
        self.text_to_data(text_element, "gender")

        ## color
        self.sele_manager.click_element('div.shop-filter-sections.color span.collapse-icon')
        text_element = self.sele_manager.get_text("div.shop-filter-sections-wrap div.shop-filter-sections.color.expanded")
        self.sele_manager.click_element('div.shop-filter-sections.color.expanded span.collapse-icon')
        self.text_to_data(text_element, "color")

        ## benefit
        text_element = self.sele_manager.get_text("div.shop-filter-sections-wrap div.shop-filter-sections.benefits.expanded")
        self.sele_manager.click_element('div.shop-filter-sections.benefits.expanded span.collapse-icon')
        self.text_to_data(text_element, "benefit")

        ## brand
        self.sele_manager.click_element('div.shop-filter-sections.brand span.collapse-icon')
        text_element = self.sele_manager.get_text("div.shop-filter-sections-wrap div.shop-filter-sections.brand.expanded")
        self.sele_manager.click_element('div.shop-filter-sections.brand.expanded span.collapse-icon')
        self.text_to_data(text_element, "brand")

        ## collection
        self.sele_manager.click_element('div.shop-filter-sections.collection span.collapse-icon')
        text_element = self.sele_manager.get_text("div.shop-filter-sections-wrap div.shop-filter-sections.collection.expanded")
        self.sele_manager.click_element('div.shop-filter-sections.collection.expanded span.collapse-icon')
        self.text_to_data(text_element, "collection")

        ## size
        self.sele_manager.click_element('div.shop-filter-sections.tag_id\[size\] span.collapse-icon')
        text_element = self.sele_manager.get_text("div.shop-filter-sections-wrap div.shop-filter-sections.tag_id\[size\].expanded")
        self.sele_manager.click_element('div.shop-filter-sections.tag_id\[size\].expanded span.collapse-icon')
        self.text_to_data(text_element, "size")
        # ## price
        self.sele_manager.scoll_down('div.shop-filter-sections.price')
        self.sele_manager.hover_click_element('div.shop-filter-sections.price span.collapse-icon')
        text_element = self.sele_manager.get_text("div.shop-filter-sections-wrap div.shop-filter-sections.price.expanded")
        self.sele_manager.click_element('div.shop-filter-sections.price.expanded span.collapse-icon')
        self.text_to_data(text_element, "price")

    def data_to_json(self):

        sorting_list = self.data_to_list('sorting')
        self.list_to_json(sorting_list, 'sorting')

        category_dic = self.data_to_dictionary('category',["아우터", "상의", "신발", "하의", "가방", "지갑", "시계", "패션잡화", "컬렉터블", "뷰티","테크", "캠핑", "가구/리빙"], case="filter", detail="category")
        self.dictionary_to_json(category_dic, 'category')

        gender_dic = self.data_to_dictionary('gender',["성별"], case="gender")
        self.dictionary_to_json(gender_dic, 'gender')

        color_dic = self.data_to_dictionary('color', ["색상"], case="color")
        self.dictionary_to_json(color_dic, 'color')

        benefit_dic = self.data_to_dictionary('benefit', ["혜택", "할인율"], case="benefit")
        self.dictionary_to_json(benefit_dic, 'benefit')

        brand_dic = self.data_to_dictionary('brand', ["브랜드"], case="brand")
        self.dictionary_to_json(brand_dic, 'brand')

        collection_dic= self.data_to_dictionary('collection', ["컬렉션"], case="collection")
        self.dictionary_to_json(collection_dic, 'collection')

        size_dic = self.data_to_dictionary('size', ["신발", "의류"], case="size")
        self.dictionary_to_json(size_dic, 'size')

        price_dic = self.data_to_dictionary('price', ["가격"], case="price")
        self.dictionary_to_json(price_dic, 'price')


if __name__ == "__main__":
    pass    

    # category_dictionary = data_manager_module.data_to_dictionary('category',["아우터", "상의", "신발", "하의", "가방", "지갑", "시계", "패션잡화", "컬렉터블", "뷰티","테크", "캠핑", "가구/리빙"], case="filter", detail="category")
    # data_manager_module.dictionary_to_json(category_dictionary, 'category')
    # gender_list = data_manager.data_to_list('gender')
    # data_manager.list_to_json(gender_list,'gender')
    # color_list = data_manager.data_to_list('color')
    # data_manager.dictionary_to_json(color_list,'color')
    # benefit_list = data_manager.data_to_list('benefit')
    # data_manager.list_to_json(benefit_list,'benefit')
    # selenium_module.save_text("div.shop-filter-sections-wrap div.shop-filter-sections.brand.expanded", filename="brand")
    # brand_list = data_manager.data_to_list('brand')
    # data_manager.list_to_json(brand_list,'brand')
    # collection_list = data_manager.data_to_list('collection')
    # data_manager.list_to_json(collection_list,'collection')
    # size_dictionary = data_manager.data_to_dictionary('size', ["신발", "의류"])
    # data_manager.list_to_json(size_dictionary,'size')
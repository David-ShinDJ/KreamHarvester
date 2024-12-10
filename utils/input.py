from utils.data_manager import DataManager

def input_login():
    email = input("이메일을 입력하세요 : ")
    password = input("비밀번호를 입력하세요 : ")
    return email, password
        
## TODO: 필터 세부 모두 선택 넣기
def input_filter():
        data_manager = DataManager()
        filters = {
            "category": "",
            "category_detail": "",
            "gender": "",
            "color": "",
            "benefit": "",
            "benefit_detail": "",
            "brand": "",
            "brand_detail": "",
            "collection": "",
            "size": "",
            "size_detail": "",
            "price": "",
            "sorting": "",
        }
        category_options = ", ".join(data_manager.json_to_dictionary('category').keys())
        category = input(f"{category_options} 중 하나를 입력하세요 : ")
        filters["category"] = category
        category_detail_options = ", ".join(data_manager.json_to_dictionary('category')[category])
        category_detail = input(f"{category_detail_options} 중 하나를 입력하세요 : ")
        filters["category_detail"] = category_detail
        gender_options = ", ".join(data_manager.json_to_list('gender')["성별"])
        gender = input(f"{gender_options} 중 하나를 입력하세요 : ")
        filters["gender"] = gender
        color_options = ", ".join(data_manager.json_to_list('color')["색상"])
        color = input(f"{color_options} 중 하나를 입력하세요 : ")
        filters["color"] = color
        benefit_options = ", ".join(data_manager.json_to_dictionary('benefit').keys())
        benefit = input(f"{benefit_options} 중 하나를 입력하세요 : ")
        benefit_detail_options = ", ".join(data_manager.json_to_dictionary('benefit')[benefit])
        benefit_detail = input(f"{benefit_detail_options} 중 하나를 입력하세요 : ")
        filters["benefit"] = benefit
        filters["benefit_detail"] = benefit_detail
        brand_options = ", ".join(data_manager.json_to_list('brand'))
        brand = input(f"{brand_options} 중 하나를 입력하세요 : ")
        filters["brand"] = brand
        brand_detail_options = ", ".join(data_manager.json_to_dictionary('brand')[brand])
        brand_detail = input(f"{brand_detail_options} 중 하나를 입력하세요 : ")
        filters["brand_detail"] = brand_detail
        collection_options = ", ".join(data_manager.json_to_list('collection'))
        collection = input(f"{collection_options} 중 하나를 입력하세요 : ")
        filters["collection"] = collection
        size_options = ", ".join(data_manager.json_to_dictionary('size').keys())
        size = input(f"{size_options} 중 하나를 입력하세요 : ")
        filters["size"] = size
        size_detail_options = ", ".join(data_manager.json_to_dictionary('size')[size])
        size_detail = input(f"{size_detail_options} 중 하나를 입력하세요 : ")
        filters["size_detail"] = size_detail
        price_options = ", ".join(data_manager.json_to_list('price'))
        price = input(f"{price_options} 중 하나를 입력하세요 : ")
        filters["price"] = price
        sorting_options = ", ".join(data_manager.json_to_list('sorting'))
        sorting = input(f"{sorting_options} 중 하나를 입력하세요 : ")
        filters["sorting"] = sorting
        return filters



def pause_while(auto_mode=True):
    """
    auto_mode가 False일 때만 사용자 입력을 기다립니다.
    True일 경우 자동으로 계속 진행됩니다.
    """
    if not auto_mode:
        while True:
            var = input("sb 중지를 멈추려면 0 입력하세요 : ")
            if var == "0":
                break

text_file_name = "self.txt"
data_path = "/Users/david/Codings/PycharmProjects/KreamHarvester/datas/"

print(data_path + text_file_name)
def pause_while():
    while True:
        var = input("sb 중지를 멈추려면 0 입력하세요 : ")
        if var == "0":
            break  # while 루프만 종료

text_file_name = "self.txt"
data_path = "/Users/david/Codings/PycharmProjects/KreamHarvester/datas/"

print(data_path + text_file_name)
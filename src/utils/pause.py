import time

def pause():
    while True:
        var = input("sb 중지를 멈추려면 0 입력하세요 : ")
        if var == "0":
            break

def pause_time(time: int):
    time.sleep(time)
def pause_while(auto_mode=True):
    """
    auto_mode가 False일 때만 사용자 입력을 기다립니다.
    True일 경우 자동으로 계속 진행됩니다.
    """
    if auto_mode:
        while True:
            var = input("sb 중지를 멈추려면 0 입력하세요 : ")
            if var == "0":
                break

if __name__ == "__main__":
    pause_while(auto_mode=False)
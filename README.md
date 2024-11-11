## Kream 자동화 프로그램
### 개요
이 프로젝트는 Python과 SeleniumBase를 사용하여 Kream 웹사이트에서 원하는 상품 정보를 자동으로 수집하고 엑셀 파일로 저장하는 웹 크롤링 프로그램입니다.

#### 주요 기능
로그인 자동화: Kream 계정으로 자동 로그인합니다.
상품 필터링: 카테고리, 브랜드, 사이즈, 가격 등 다양한 조건으로 상품을 필터링합니다.
상품 정보 추출: 상품명, 가격, 이미지, 사이즈, 판매자 정보 등을 추출합니다.
데이터 저장: 추출된 정보를 엑셀 파일로 저장합니다.
headless 모드: 백그라운드에서 실행하여 브라우저 창을 띄우지 않습니다.
##### 사용 방법
환경 설정:
Python 3.7 이상 설치
requirements.txt 파일의 라이브러리 설치 (pip install -r requirements.txt)
ChromeDriver 설치 및 경로 설정
config.py 파일에서 Kream 계정 정보 (이메일, 비밀번호) 설정

###### 실행:
main.py 파일 실행
프로그램 실행 중에 필요한 정보 (카테고리, 필터 등) 입력
크롤링 완료 후 products.xlsx 파일 확인
###### 코드 구조
main.py: 프로그램 실행 및 제어
login.py: Kream 로그인 기능
crawler.py: 상품 정보 크롤링 및 데이터 처리
utils.py: 유틸리티 함수
config.py: 설정 값 저장
라이브러리
SeleniumBase: 웹 테스트 자동화 및 웹 스크래핑
parameterized: 테스트 함수에 여러 인자 전달
logging: 프로그램 실행 로그 기록
주의 사항
Kream 웹사이트 robots.txt 준수
과도한 크롤링 자제
Kream 웹사이트 구조 변경 시 코드 수정 필요
기여
이슈 제기 및 pull request 환영

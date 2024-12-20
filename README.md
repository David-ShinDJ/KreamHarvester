# Kream 자동화 프로그램
### 개요
이 프로젝트는 Python과 SeleniumBase를 사용하여 Kream 웹사이트에서 원하는 상품 정보를 자동으로 수집하고 엑셀 파일로 저장하는 웹 크롤링 프로그램입니다.

#### 주요 기능
로그인 자동화: Kream 계정으로 자동 로그인합니다.
상품 필터링: 카테고리, 브랜드, 사이즈, 가격 등 다양한 조건으로 상품을 필터링합니다.
상품 정보 추출: 상품명, 가격, 이미지, 사이즈, 판매자 정보 등을 추출합니다.
데이터 저장: 추출된 정보를 엑셀 파일로 저장합니다.
##### 사용 방법
환경 설정:
Python 3.7 이상 설치
ChromeDriver 설치 및 경로 설정
###### 설계방식:
Test Driven Development 기반으로 기능구현에 대한 Test Module 작성후 pytest 테스트 통과후 Core Module 작성 Core Module 실행후 각모듈의 연결이 완료되면 다시 Test Module 작성
###### 실행:
main.py 파일 실행
프로그램 실행 중에 필요한 정보 (카테고리, 필터 등) 입력
크롤링 완료 후 products.xlsx 파일 확인
###### 코드 구조
main.py: 프로그램 실행 및 제어
Core - 실제코드기능구현 
Utils - 서브기능 ex) bs4 html 작성 
Pages - Kream HTMl 소스코드
Test - 테스트코드 BaseCase 작성
###### 라이브러리
SeleniumBase: 웹 테스트 자동화 및 웹 스크래핑 핵심기능담당
Selenium: 크롬드라이버 기능설정
bs4: 페이지 소스코드 크롤링
###### 주의 사항
Kream 웹사이트 robots.txt 준수
Kream 웹사이트 구조 변경 시 코드 수정 필요
### 기여
이슈 제기 및 pull request 환영

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SeleniumManager:

    def __init__(self):
        options = Options()
        # options.add_argument("--headless") // 활성화 find_element selector 못 찾는 이슈
        options.add_argument("start-maximized")
        self.driver = webdriver.Chrome(service=Service(executable_path='/Users/david/ExternalApp/chromedriver-mac-arm64/chromedriver'), options=options)
        self.driver.implicitly_wait(15)
        self.wait = WebDriverWait(self.driver, 10)
        print("드라이버가 성공적으로 시작되었습니다.")

    def open_url(self, url):
        try:
            self.driver.get(url)
            print(f"{url} 로드 완료")
        except Exception as e:
            print(f"{url} 페이지 로드 실패. 오류: {e}")

    def _find_element(self, selector, by=By.CSS_SELECTOR):
        try:
            element = self.driver.find_element(by, selector)
            print(f"{selector}를 바로 찾았습니다.")
            return element
        except Exception as e:
            print(f"{selector}를 바로 찾을 수 없습니다. 오류: {e}")
            return None

    def _find_elements(self, selector, by=By.CSS_SELECTOR):
        try:
            elements = self.driver.find_elements(by, selector)
            print(f"{selector} 모두를 바로 찾았습니다.")
            return elements
        except Exception as e:
            print(f"{selector} 모두를 바로 찾을 수 없습니다. 오류: {e}")
            return None

    def wait_for_element(self, selector, by=By.CSS_SELECTOR):
        """
        요소가 나타날 때까지 기다립니다.

        Args:
            selector: CSS selector 또는 XPath 문자열
            by: By.CSS_SELECTOR 또는 By.XPATH

        Returns:
            WebElement 또는 None
        """
        try:
            element = self.wait.until(EC.presence_of_element_located((by, selector)))
            print(f"{selector}를 찾았습니다.")
            return element
        except Exception as e:
            print(f"{selector}를 찾는 데 실패했습니다. 오류: {e}")
            return None

    def wait_for_elements(self, selector, by=By.CSS_SELECTOR):
        """
        여러 요소가 나타날 때까지 기다립니다.

        Args:
            selector: CSS selector 또는 XPath 문자열
            by: By.CSS_SELECTOR 또는 By.XPATH

        Returns:
            WebElement 리스트 또는 None
        """
        try:
            elements = self.wait.until(EC.presence_of_all_elements_located((by, selector)))
            print(f"{selector} 모두를 찾았습니다.")
            return elements
        except Exception as e:
            print(f"{selector} 모두를 찾는 데 실패했습니다. 오류: {e}")
            return None

    def click_element(self, selector, by=By.CSS_SELECTOR):
        """
        요소를 클릭합니다.

        Args:
            selector: CSS selector 또는 XPath 문자열
            by: By.CSS_SELECTOR 또는 By.XPATH
        """
        element = self._find_element(selector, by)
        if not element:
            element = self.wait_for_element(selector, by)
        if element:
            try:
                element.click()
                print(f"{selector}를 클릭했습니다.")
            except Exception as e:
                print(f"{selector}를 클릭하지 못했습니다. 오류: {e}")
        else:
            print(f"요소를 찾을 수 없습니다: {selector}")

    def get_text(self, selector, by=By.CSS_SELECTOR):
        element = self._find_element(selector, by)
        if not element:
            element = self.wait_for_element(selector, by)
        try:
            text = element.text
            print(f"{selector} 텍스트 가져오기 성공")
            return text
        except Exception as e:
            print(f"{selector} 텍스트 가져오기 실패. 오류: {e}")
            return None
    ## 
    def get_text_element(self, selector, by=By.CSS_SELECTOR):
        text_element = self.get_text(selector, by)
        if text_element:
            return text_element
        else:
            return None

    def get_current_url(self):
        """현재 URL을 반환합니다."""
        return self.driver.current_url

    def quit_driver(self):
        """웹 드라이버를 종료합니다."""
        self.driver.quit()
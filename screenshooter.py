import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class GoogleKeywardScreenShooter():
    def __init__(self, keyward, directory):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.keyward = keyward
        self.directory = directory

    def start(self):
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

        # google로 접속
        self.browser.get("https://google.com")

        # 검색창 찾은 후 입력, 엔터
        search_bar = self.browser.find_element_by_class_name("gLFyf")
        search_bar.send_keys(self.keyward)
        search_bar.send_keys(Keys.ENTER)

        needToRemoveElement = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "g-blk")))

        self.browser.execute_script("""
            const payload = arguments[0]
            console.log(payload)
            payload.parentElement.removeChild(payload)
        """, needToRemoveElement)

        search_results = self.browser.find_elements_by_class_name("g")
        for index, search_result in enumerate(search_results):
            search_result.screenshot(
                f"{self.directory}/{self.keyward}x{index}.png")

        self.browser.quit()


GoogleSShooter = GoogleKeywardScreenShooter("buy domain", "output")
GoogleSShooter.start()

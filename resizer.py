import time
import math
import os

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class ResponsiveTester():

    def __init__(self, url, directory):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser.maximize_window()
        self.url = url
        self.directory = directory
        self.sizes = [480, 960, 1366, 1920]

    def start(self):
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

        BROWSER_HEIGHT = 1027
        self.browser.get(self.url)

        for size in self.sizes:
            self.browser.set_window_size(size, BROWSER_HEIGHT)
            # 우선 새로운 사이즈로 브라우저를 변경하면 처음으로 올려야 스크롤을 다시 내리겠죠
            self.browser.execute_script("window.scrollTo(0, 0)")

            # 새로운 스크롤 이동 후 스크롤을 최상단으로 올라왔을 때 곧바로 진행하면 스크린샷을 못 찍는 경우가 있습니다. 잠시 ㄱㄷ
            time.sleep(2)
            # 브라우저 전체 높이를 구합시다.
            scroll_size = self.browser.execute_script(
                "return document.body.scrollHeight")
            # 브라우저 전체 높이/ 스크롤 높이를 나눈 수 만큼 스크롤을 내릴 겁니다.
            total_sections = (math.ceil(scroll_size / BROWSER_HEIGHT))

            # 스크롤 수 만큼 내리면서 스크린샷을 찍습니다.
            for section in range(total_sections + 1):
                self.browser.execute_script(f"""
                    window.scrollTo(0, {(section) * BROWSER_HEIGHT})
                """)
                self.browser.save_screenshot(
                    f"{self.directory}/{size}x{section}.png")


tester = ResponsiveTester("https://nomadcoders.co", "resizer")
tester.start()

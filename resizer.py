import time
import math
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())
BROWSER_HEIGHT = 1027

browser.get("https://nomadcoders.co")
browser.maximize_window()

sizes = [480, 960, 1366, 1920]

for size in sizes:
    browser.set_window_size(size, BROWSER_HEIGHT)
    scroll_size = browser.execute_script("""
        return document.body.scrollHeight;
    """)
    total_sections = (math.ceil(scroll_size / BROWSER_HEIGHT))
    for section in range(total_sections):
        browser.execute_script(f"""
            window.scrollTo(0, {(section + 1) * BROWSER_HEIGHT})
        """)
        time.sleep(3)

    time.sleep(3)

import time
import random

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class SeleniumDriver:

    def __init__(self, port=random.randrange(9000, 9999), url='https://google.com', profil=False, inconito=False,
                 headless=False) -> None:
        super().__init__()
        options = Options()
        # options.add_experimental_option("debuggerAddress", "127.0.0.1:" + str(port))
        options.add_argument("--remote-debugging-port=" + str(port))
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-browser-side-navigation")
        if profil is True:
            options.add_argument(
                "user-data-dir=C:\\Users\\Conta\\AppData\\Local\\Google\\Chrome\\User Data")
        if inconito is True:
            options.add_argument('--incognito')
        if headless is True:
            options.add_argument('--headless')
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-features=VizDisplayCompositor")
        self.driver = webdriver.Chrome(options=options)
        print('driver lunched')
        self.action = ActionChains(self.driver)
        self.driver.get(url)
        # self.driver.maximize_window()
        time.sleep(1)
        try:
            self.driver.find_element(By.CSS_SELECTOR, '#L2AGLb').click()
            time.sleep(1)
        except:
            pass
        return
    
    # ------------ Security ---------------

    def captcha(self) -> None:
        captcha_selector = '.Captcha, .captcha, #Captcha, #captcha, .pass-Captcha'
        if "checkpoint" in self.driver.current_url or "challenge" in self.driver.current_url or self.is_attached(captcha_selector):
            print('captcha')
            while "checkpoint" in self.driver.current_url or "challenge" in self.driver.current_url or self.is_attached(captcha_selector):
                time.sleep(2)
                print('wait')
        return
    
    # ------------ Elements ---------------

    def find_element(self, css_selector):
        for _ in range(3):
            try:
                return self.driver.find_element(By.CSS_SELECTOR, css_selector)
            except:
                time.sleep(1)

    def find_elements(self, css_selector):
        for _ in range(3):
            try:
                return self.driver.find_elements(By.CSS_SELECTOR, css_selector)
            except:
                time.sleep(1)

    def is_attached(self, css_selector) -> bool:
        for _ in range(3):
            try:
                if len(self.driver.find_elements(By.CSS_SELECTOR, css_selector)) > 0:
                    return True
            except:
                time.sleep(1)
        return False
    
    # ------------ Window ---------------

    def window_handles(self):
        return self.driver.window_handles

    def switch_to_window(self, window=None):
        if window is None:
            return
        self.driver.switch_to.window(window)

    def close(self):
        self.driver.close()

    # ------------ USER ACTION ---------------

    def get(self, url) -> None:
        print(f'get | {url}')
        self.driver.get(url)
        return

    def execute_script(self, script) -> None:
        try:
            self.driver.execute_script(script)
        except:
            pass
        return

    def click(self, css_selector) -> bool:
        time.sleep(1)
        print(f'click | {css_selector}')
        try:
            element = self.driver.find_element(By.CSS_SELECTOR, css_selector)
            self.action.move_to_element(element).click().perform()
        except:
            print('error')
            return False
        return True

    def write(self, css_selector, string) -> bool:
        self.click(css_selector)
        time.sleep(1)
        print(f'write | {css_selector}')
        self.execute_script(f"document.querySelector('{css_selector}').value = ''")
        for letter in string:
            try:
                self.driver.find_element(
                    By.CSS_SELECTOR, css_selector).send_keys(letter)
                time.sleep(random.randrange(1, 4)/10)
            except:
                print('error')
                return False
        return True

    # ------------ USER ACTION ---------------

    def current_url(self) -> str:
        return self.driver.current_url

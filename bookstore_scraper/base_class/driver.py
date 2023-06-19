from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service


class Driver:
    def __init__(self, headless=False):
        folder = 'D:\downloads'
        options = ChromeOptions()
        prefs = {
            'download.default_directory': folder,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing_for_trusted_sources_enabled": False,
            "safebrowsing.enabled": False
        }
        if headless:
            options.add_argument("--headless=new")

        options.add_experimental_option("prefs", prefs)
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver_path = ChromeDriverManager().install()
        service = Service(executable_path=driver_path)
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.maximize_window()

    def url_get(self, url):
        self.driver.get(url)

    def load_page(self, page, url='', wait_time=60):
        if url != '':
            self.driver.get(url)
        try:
            WebDriverWait(self.driver, wait_time).until(
                lambda driver: driver.execute_script("return document.readyState") == "complete"
            )
            print(f"{page} page loaded")
        except TimeoutException:
            print(f"{page} Loading taking too much time")
            raise

    def click_button(self, xpath, by_type=By.XPATH, wait_time=60):
        try:
            WebDriverWait(self.driver, wait_time).until(EC.presence_of_element_located(by_type, xpath))
            self.driver.find_element(by_type, xpath).click()
        except Exception:
            print("Element cannot be clicked")

    def find_element(self, xpath, by_type=By.XPATH, wait_time=60):
        try:
            WebDriverWait(self.driver, wait_time).until(EC.presence_of_element_located((by_type, xpath)))
            return self.driver.find_element(by_type, xpath)
        except Exception:

            print("oops Element not found")

    def execute_script(self, script, *args):
        try:
            return self.driver.execute_script(script, *args)
        except Exception as e:
            print("An error occurred:", str(e))

    def scroll(self, xpath):
        sc = self.find_element(xpath, By.XPATH)
        return self.execute_script("arguments[0].scrollIntoView();", sc)

    def scroll_into_view(self, element):
        element.location_once_scrolled_into_view

    def __del__(self):
        self.driver.close()

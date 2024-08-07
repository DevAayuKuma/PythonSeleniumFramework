#from lib2to3.pgen2 import driver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from utilities.Baseclass import Baseclass
from selenium.webdriver.support import expected_conditions


class TestOne(Baseclass):

    def test_one(self):
        self.driver.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox").send_keys("iphone 14 128gb")
        self.driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']").click()
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Apple iPhone 14 (512 GB) - Yellow']").click()

        windowsOpened = self.driver.window_handles

        self.driver.switch_to.window(windowsOpened[1])
        secondtab = self.driver.title
        self.driver.implicitly_wait(5)
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.title_contains(secondtab))
        Amazon_price = self.driver.find_element(By.XPATH, "//span[normalize-space()='86,994']").text
        print(Amazon_price)

#time.sleep(5)

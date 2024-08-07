#from lib2to3.pgen2 import driver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from utilities.Baseclass import Baseclass
from selenium.webdriver.support import expected_conditions


class TestTwo(Baseclass):

    def test_two(self):
        self.driver.get("https://www.flipkart.com/")
        self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search for Products, Brands and More']").send_keys("iphone 14 128gb yellow")
        self.driver.find_element(By.CSS_SELECTOR, "svg[width='24']").click()
        self.driver.find_element(By.XPATH, "//div[normalize-space()='Apple iPhone 14 (Yellow, 128 GB)']").click()

        windowsOpened = self.driver.window_handles

        self.driver.switch_to.window(windowsOpened[1])
        secondtab = self.driver.title
        self.driver.implicitly_wait(5)
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.title_contains(secondtab))
        flipkart_price = self.driver.find_element(By.XPATH,"//div[@class='Nx9bqj CxhGGd']").text
        print(flipkart_price)

#time.sleep(5)

# Go to https://www.amazon.in.
# 2. Once page is loaded, search for iPhone XR (64GB) - Yellow.
# 3. Select the matching iPhone once list appears.
# 4. Get the price of the selected iPhone.
# 5. Now, go to https://www.flipkart.com/.
# 6. Repeat steps 2 to 4 and get the price.
# 7. Compare the price on both the website and determine which website.
# has lesser value for the iPhone and print the final result on the console.

import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
import time

from selenium.webdriver.common.by import By


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.get("https://www.amazon.in./")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

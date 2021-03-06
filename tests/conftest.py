from selenium import webdriver
import pytest

@pytest.fixture
def selenium_driver():
    driver = webdriver.Chrome(
        executable_path="C:/Users/843974/PycharmProjects/Python_html_report/drivers/chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(2)
    yield driver
    driver.quit()
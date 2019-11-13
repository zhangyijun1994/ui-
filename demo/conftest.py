from asyncio import sleep
from selenium import webdriver
import pytest

@pytest.fixture(scope='session')
def driver():
    # 打开浏览器
    driver = webdriver.Chrome('../chrome_driver_v78/chromedriver.exe')

    # 调整浏览器窗口大小
    driver.maximize_window()
    yield driver
    driver.quit()
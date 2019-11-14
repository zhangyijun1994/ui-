from asyncio import sleep
from time import sleep

import autoit
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #定义了变量EC表示expected_conditions


# 消息提示
def test_text(driver):
    driver.get("http://ui.yansl.com/#/message")
    # 定位到“自动关闭提示”中的“消息”模块.多元素+s,elements
    buttons = driver.find_elements_by_xpath("//label[contains(text(),'自动关闭提示')]/..//span[text()='消息']")
    buttons[0].click()  #取模块下标0（0消息）
    # 再定位到提示信息
    message = driver.find_element_by_xpath("//div[@role='alert']/p")
    text = message.text # text+方法  获取展示文本
    print(text)
    assert"这是一条消息" in text # 断言assert "内容" in next
    sleep(2)

#
def test_page_source(driver):
    driver.get("http://ui.yansl.com/")
    #获取“通知提示”模块
    driver.find_element_by_xpath('//*[@id="app"]/section/section/aside/ul/li[3]/div').click()
    sleep(2)
    #获取“消息提示”模块
    driver.find_element_by_xpath("//li[contains(text(),'消息提示')]").click()
    sleep(2)
    # 获取页面源代码
    sourse = driver.page_source
    print(sourse)
    assert"手工关闭提示" in sourse
    sleep(10)
from asyncio import sleep
from time import sleep

import autoit
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #定义了变量EC表示expected_conditions


def test_input(driver):
    driver.get("http://ui.yansl.com/#/input")
    sleep(2)

    input = driver.find_element_by_xpath("//input[@name='t1']")
    #清空
    input.clear()   #清除INPUT处原本的内容
    #输入
    input.send_keys("我是谁？我在哪？我叫什么")
    sleep(2)

# 单选框
def test_radio(driver):
    driver.get("http://ui.yansl.com/#/radio")
    sleep(2)

    radio = driver.find_element_by_xpath("//input[@name='sex'][2]")
    # 点击
    radio.click()
    sleep(2)

# 多选
def test_checkbox(driver):
    driver.get("http://ui.yansl.com/#/checkbox")
    sleep(2)

    checkbox = driver.find_element_by_xpath("//*[@id='form']/form/div[2]/div/div/label[1]/span[1]/span")
    attribute = checkbox.get_attribute("class")  #获取在多选框元素里的“CLASS”
    if not attribute=='el-checkbox__input is-checked':  #如果attribute不是在被选中的状态
        checkbox.click()
        sleep(5)
    checkbox = driver.find_element_by_xpath("//*[@id='form']/form/div[2]/div/div/label[1]/span[1]/span")
    attribute = checkbox.get_attribute("class")  #获取在多选框元素里的“CLASS”
    if not attribute=='el-checkbox__input is-checked':    #如果attribute不是在被选中的状态
        checkbox.click()
        sleep(5)


# 下拉框
def test_select(driver):
    driver.get("http://ui.yansl.com/#/select")
    sleep(2)

    select = driver.find_element_by_xpath("//*[@id='form']/form/div[3]/div/div/div[2]/input")
    # 点击
    select.click()

    sleep(2)
    option = driver.find_element_by_xpath("(//span[text()='双皮奶'])[last()]")
    actions = ActionChains(driver)   #执行鼠标操作的命令
    actions.move_to_element(option).perform()   #鼠标移动到元素.运行
    sleep(2)
    option.click()


#滑块#
def test_slider(driver):
    driver.get("http://ui.yansl.com/#/slider")
    sleep(2)

    slider = driver.find_element_by_xpath("//*[@id='form']/form/div[5]/div/div/div/div[2]/div")
    sleep(2)
    actions = ActionChains(driver)
    actions.drag_and_drop_by_offset(slider,0,-200).perform()
    #在SLIDER元素里拖拽到0，-200的坐标.执行
    sleep(2)

# 时间
def test_time(driver):
    driver.get("http://ui.yansl.com/#/dateTime")
    sleep(2)

    t1 = driver.find_element_by_xpath("//*[@id='form']/form/div[1]/div[1]/div/div/input")
    #清空
    t1.clear()   #清除TL处原本的内容
    #输入
    t1.send_keys("14:14:14")
    sleep(2)

# 上传
def test_file(driver):
    driver.get("http://ui.yansl.com/#/upload")
    sleep(2)

    file = driver.find_element_by_xpath("//*[@id='form']/form/div[1]/div/input")
    # 清空
    file.clear()
    # 输入
    file.send_keys("C:\\Users\\guoya\\Desktop\\11.png")
    sleep(2)


def test_file2(driver):
    driver.get("http://ui.yansl.com/#/upload")
    sleep(2)

    file = driver.find_element_by_xpath("//*[@id='form']/form/div[2]/div/div/div[1]/button")
    file.click()
    sleep(2)
    autoit.win_wait("打开", 10)
    sleep(1)
    # autoit.control_send("打开", "Edit1", os.path.abspath(file_path))
    autoit.control_set_text("打开", "Edit1", "C:\\Users\\guoya\\Desktop\\11.png")
    sleep(2)
    autoit.control_click("打开", "Button1")
    sleep(2)

# 弹窗
def test_alert(driver):
    driver.get("http://192.168.1.128:8082/xuepl/demo.html")
    sleep(2)

    button = driver.find_element_by_xpath("/html/body/table/tbody/tr[6]/td[2]/input")
    button.click()
    sleep(2)
    alert = driver.switch_to.alert   #固定格式    弹窗切换，切换到弹窗里
    alert.send_keys("fsjdfhldsf")   #输入fsjdfhldsf
    alert.accept()  #弹窗里接受
    sleep(2)

# 超链接
def test_windows(driver):
    driver.get("http://192.168.1.128:8082/xuepl/demo.html")
    sleep(2)

    dang_dang = driver.find_element_by_link_text("当当") #准确定位“当当”
    actions = ActionChains(driver)  #类的实例化，当需要同时用键盘和鼠标的时候用到
    actions.key_down(Keys.CONTROL).click(dang_dang).key_up(Keys.CONTROL).perform()
    # 同时按住CTRL并且点击当当，松开CTRL，运行
    sleep(2)

    jd = driver.find_element_by_link_text("京东")   #准确定位“京东”
    actions = ActionChains(driver)  #类的实例化，当需要同时用键盘和鼠标的时候用到
    actions.key_down(Keys.CONTROL).click(jd).key_up(Keys.CONTROL).perform()
    sleep(2)

    dn = driver.find_element_by_partial_link_text("度娘")    #模糊定位“度娘”
    actions = ActionChains(driver)  #类的实例化，当需要同时用键盘和鼠标的时候用到
    actions.key_down(Keys.CONTROL).click(dn).key_up(Keys.CONTROL).perform()
    #同时按住CTRL并且点击度娘，松开CTRL，运行
    sleep(2)

    # 获取所有窗口的句柄
    handles = driver.window_handles
    for h in handles:
        # 根据窗口句柄，切换窗口
        driver.switch_to.window(h)     # 弹窗
        sleep(2)
        if driver.title.__contains__("京东"):  # 如果标题里包含“京东”
            break    # 终止

# 嵌套切换
def test_iframe(driver):
    driver.get("http://192.168.1.128:8082/xuepl1/frame/main.html")

    frame = driver.find_element_by_xpath("/html/frameset/frameset/frame[1]") # 进入到当前的iframe模块(左侧模块)
    driver.switch_to.frame(frame)  # 涉及到切换模块用frame

    driver.find_element_by_partial_link_text('京东').click() # 点击京东的文字按钮

    # 退出当前iframe
    driver.switch_to.parent_frame()
    # 回到初始页面
    # driver.switch_to.default_content()

    iframe = driver.find_element_by_xpath("/html/frameset/frameset/frame[2]") # 进入到当前的iframe模块(京东模块)
    driver.switch_to.frame(iframe) # 涉及到切换模块用frame

    inpu = driver.find_element_by_xpath('//*[@id="key"]')  # 选定输入框
    inpu.clear()
    inpu.send_keys("手机")  # 输入文本“手机”

# 显示等待
def test_wait(driver):
    driver.get("http://ui.yansl.com/#/loading")
    bt = driver.find_element_by_xpath("//span[contains(text(),'指令方式')]")
    bt.click()
    WebDriverWait(driver,5,0.5).until(
        EC.visibility_of_element_located((By.XPATH,'//tbody/tr[1]/td[2]/div'))
    )
    bg = driver.find_element_by_xpath("//tbody/tr[1]/td[2]/div")
    print(bg.text)
    sleep(2)

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
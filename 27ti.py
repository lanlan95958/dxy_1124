# 需求：对《注册实例.html》进行信息注册
# 账号：admin,密码：123456，电话：18600000000，
# 电子邮件：123@qq.com 要求： 1. 对注册《主界面、注册A、注册B》
# 三个注册信息进行注册信息填写 2. 定位方式不限 3. 暂停3秒钟关闭浏览器

from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get(r"file:///C:/Users/du/Desktop/注册/注册实例.html")

driver.find_element_by_id("user").send_keys("admin")
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_id("tel").send_keys("18600000000")
driver.find_element_by_id("email").send_keys("123@qq.com")

# driver.switch_to.window(driver.window_handles[0])
driver.switch_to.frame("myframe1")

driver.find_element_by_id("userA").send_keys("admin")
driver.find_element_by_id("passwordA").send_keys("123456")
driver.find_element_by_id("telA").send_keys("18600000000")
driver.find_element_by_id("emailA").send_keys("123@qq.com")

# driver.switch_to.window(driver.window_handles[0])
driver.switch_to.default_content()

driver.switch_to.frame("myframe2")

driver.find_element_by_id("userB").send_keys("admin")
driver.find_element_by_id("passwordB").send_keys("123456")
driver.find_element_by_id("telB").send_keys("18600000000")
driver.find_element_by_id("emailB").send_keys("123@qq.com")

time.sleep(3)
driver.quit()

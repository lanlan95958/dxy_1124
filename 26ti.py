# 需求：对《注册A.html》进行信息注册 账号：admin,密码：123456，
# 电话：18600000000，电子邮件：123@qq.com 要求： 1.
#  定位方式统一使用CSS定位 2. 暂停2秒钟点击注册用户A按钮
# 3.暂停3秒钟后关闭浏览器
from  selenium import  webdriver
import  time

driver = webdriver.Firefox()
driver.get(r"file:///C:/Users/du/Desktop/注册/注册A.html")
driver.find_element_by_css_selector("#userA").send_keys("admin")
driver.find_element_by_css_selector("#passwordA").send_keys("123456")
driver.find_element_by_css_selector("#telA").send_keys("18600000000")
driver.find_element_by_css_selector("#emailA").send_keys("123@qq.com")
time.sleep(2)
driver.find_element_by_css_selector("#zc>fieldset>button").click()

time.sleep(3)
driver.quit()

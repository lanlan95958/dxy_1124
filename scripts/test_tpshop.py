# 需求：对TPshop/iweb_shop项目进行前台登录设计脚本
# 要求：
# 1. 使用unittest框架
# 2. 使用Fixture(setup、tearDown)
# 3. 浏览器最大化、隐式等待30秒
# 4. 使用断言判断登录用户是否为admin，不是则截屏保存图片
# 5. 图片命名格式为脚本执行时间
import  unittest
from selenium import webdriver
class TestTpShop(unittest.TestCase):

    def setUp(self):
        self.dirver = webdriver.Firefox()
        self.dirver.get(r"http://127.0.0.1/index.php")
        self.dirver.maximize_window()
        self.dirver.implicitly_wait(30)

    def test_tpshop(self):
        self.dirver.find_element_by_class_name("red").click()
        self.dirver.find_element_by_id("username").send_keys("admin")
        self.dirver.find_element_by_id("password").send_keys("123456")
        self.dirver.find_element_by_id("verify_code").send_keys("8888")
        self.dirver.find_element_by_class_name("J-login-submit").click()
        res1="admin"
        res2=self.dirver.find_element_by_xpath("html/body/div[1]/div/div/div/div[2]/a[1]").text

        if res1 ==res2:
            print("断言继续进行")

        else: self.dirver.get_screenshot_as_file("脚本执行时间.png")


    def tearDown(self):

        self.dirver.quit()




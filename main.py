# 需求：对TPshop/iweb_shop项目进行前台登录设计脚本
# 要求：
# 1. 使用unittest框架
# 2. 使用Fixture(setup、tearDown)
# 3. 浏览器最大化、隐式等待30秒
# 4. 使用断言判断登录用户是否为admin，不是则截屏保存图片
# 5. 图片命名格式为脚本执行时间
from selenium import  webdriver
import time
import  unittest
if __name__ == '__main__':

        suite = unittest.defaultTestLoader.discover("./scripts","test_*.py")
        unittest.TextTestRunner().run(suite)
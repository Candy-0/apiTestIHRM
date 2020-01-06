import unittest
import logging
from api.login_api import LoginAPI
from utils import assert_common


class TestIHRMLogin(unittest.TestCase):
    """测试IHRM登录类"""

    def setUp(self) -> None:
        pass

    @classmethod
    def setUpClass(cls) -> None:
        cls.login_api = LoginAPI()

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test01_login_success(self):
        """登录成功测试方法"""
        response = self.login_api.get_login_url("13800000002", "123456")
        # 接收返回的json数据
        jsonData = response.json()
        # 调试输出登录接口的数据
        logging.info("登录成功接口返回的数据为：{}".format(jsonData))

        # 断言
        # self.assertEqual(200,response.status_code)  # 断言响应状态码
        # self.assertEqual(True,jsonData.get("success")) # 断言json响应数据中的success
        # self.assertEqual(10000,jsonData.get("code"))  # 断言json响应数据中的code
        # self.assertIn("操作成功",jsonData.get("message"))  # 断言json响应数据中的message
        assert_common(self, response, 200, True, 10000, "操作成功")

    def test02_username_is_not_exist(self):
        """用户不存在测试方法"""
        response = self.login_api.get_login_url("13900000002", "123456")
        # 接收返回的json数据
        jsonData = response.json()
        # 调试输出登录接口的数据
        logging.info("用户不存在接口返回的数据为：{}".format(jsonData))
        # 断言
        assert_common(self, response, 200, False, 20001, "用户名或密码错误")

    def test03_password_error(self):
        """密码错误测试方法"""
        response = self.login_api.get_login_url("13800000002", "error")
        # 接收返回的json数据
        jsonData = response.json()
        # 调试输出登录接口的数据
        logging.info("密码错误接口返回的数据为：{}".format(jsonData))
        # 断言
        assert_common(self, response, 200, False, 20001, "用户名或密码错误")

    def test04_empty_username(self):
        """用户名为空测试方法"""
        response = self.login_api.get_login_url("", "123456")
        # 接收返回的json数据
        jsonData = response.json()
        # 调试输出登录接口的数据
        logging.info("用户名为空接口返回的数据为：{}".format(jsonData))
        # 断言
        assert_common(self, response, 200, False, 20001, "用户名或密码错误")

    def test05_username_contains_special_character(self):
        """账号包含特殊字符测试方法"""
        response = self.login_api.get_login_url("!@#$%^&*()*", "123456")
        # 接收返回的json数据
        jsonData = response.json()
        # 调试输出登录接口的数据
        logging.info("账号包含特殊字符接口返回的数据为：{}".format(jsonData))
        # 断言
        assert_common(self, response, 200, False, 20001, "用户名或密码错误")

    def test06_empty_password(self):
        """密码为空测试方法"""
        response = self.login_api.get_login_url("13800000002", "")
        # 接收返回的json数据
        jsonData = response.json()
        # 调试输出登录接口的数据
        logging.info("密码为空接口返回的数据为：{}".format(jsonData))
        # 断言
        assert_common(self, response, 200, False, 20001, "用户名或密码错误")

    def test07_username_contains_chinese(self):
        """账号包含中文测试方法"""
        response = self.login_api.get_login_url("13中00000002", "123456")
        # 接收返回的json数据
        jsonData = response.json()
        # 调试输出登录接口的数据
        logging.info("账号包含中文接口返回的数据为：{}".format(jsonData))
        # 断言
        assert_common(self, response, 200, False, 20001, "用户名或密码错误")

    def test08_username_contains_space(self):
        """账号包含空格测试方法"""
        response = self.login_api.get_login_url("13 000 0002", "123456")
        # 接收返回的json数据
        jsonData = response.json()
        # 调试输出登录接口的数据
        logging.info("账号包含空格接口返回的数据为：{}".format(jsonData))
        # 断言
        assert_common(self, response, 200, False, 20001, "用户名或密码错误")


if __name__ == '__main__':
    unittest.main()

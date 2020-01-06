import unittest
import logging
from api.login_api import LoginAPI
from utils import assert_common, read_login_data
from parameterized import parameterized


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

    @parameterized.expand(read_login_data)
    def test_login(self, mobile, password, http_code, success, code, message):
        """登录测试方法"""
        response = self.login_api.get_login_url(mobile, password)
        # 接收返回的json数据
        jsonData = response.json()
        # 调试输出登录接口的数据
        logging.info("登录接口返回的数据为：{}".format(jsonData))
        # 断言
        assert_common(self, response, http_code, success, code, message)


if __name__ == '__main__':
    unittest.main()

import unittest
import logging
from api.login_api import LoginAPI
from utils import assert_common
import app


class TestLogin(unittest.TestCase):
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

    def test_login_success(self):
        """登录测试方法"""
        response = self.login_api.get_login_url("13800000002", "123456")
        # 接收返回的json数据
        jsonData = response.json()
        # 调试输出登录接口的数据
        logging.info("登录成功接口返回的数据为：{}".format(jsonData))
        # 断言
        assert_common(self, response, 200, True, 10000, "操作成功")
        # 获取令牌，并将令牌添加到HEADERS中
        token = jsonData.get('data')
        app.HEADERS["Authorization"] = "Bearer " + token
        logging.info("获取的令牌为：{}".format(app.HEADERS))

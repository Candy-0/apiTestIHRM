import unittest
import logging
from parameterized import parameterized
import app
from api.emp_api import EmpAPI
from utils import assert_common
import utils
import pymysql


class TestIHRMEmp(unittest.TestCase):
    """测试IHRM员工类"""

    def setUp(self) -> None:
        pass

    @classmethod
    def setUpClass(cls) -> None:
        cls.emp_api = EmpAPI()

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    @parameterized.expand(utils.read_add_emp_json())
    def test01_add_emp(self, mobile, username, http_code, success, code, message):
        """测试添加员工方法"""
        # 调用员工接口
        response = self.emp_api.add_emp(mobile, username)
        # 获取添加员工接口的json数据
        jsonData = response.json()
        # 输出json数据
        logging.info("添加员工接口返回的数据为：{}".format(jsonData))
        # 断言
        assert_common(self, response, http_code, success, code, message)

        # 获取员工id并添加到全局变量
        app.EMP_ID = jsonData.get("data").get("id")
        # 输出员工id
        logging.info("员工id为：{}".format(app.EMP_ID))

    @parameterized.expand(utils.read_query_emp_json())
    def test02_query_emp(self, http_code, success, code, message):
        """测试查询员工方法"""
        # 调用查询员工接口
        response = self.emp_api.query_emp()
        # 获取查询员工的json数据
        jsonData = response.json()
        # 输出数据
        logging.info("查询员工接口返回的数据为：{}".format(jsonData))
        # 断言
        assert_common(self, response, http_code, success, code, message)

    @parameterized.expand(utils.read_update_emp_json())
    def test03_update_emp(self, username, http_code, success, code, message):
        """测试修改员工方法"""
        # 调用修改员工接口
        response = self.emp_api.update_emp(username)
        # 获取修改员工的json数据
        jsonData = response.json()
        # 输出数据
        logging.info("修改员工接口返回的数据为：{}".format(jsonData))

        # # 建立连接
        # conn = pymysql.connect("182.92.81.159","readuser","iHRM_user_2019","ihrm")
        # # 获取游标
        # cursor = conn.cursor()

        with utils.DBUtils() as db_utils:
            # 执行sql语句
            sql = "select username from bs_user where id={}".format(app.EMP_ID)
            db_utils.execute(sql)
            result = db_utils.fetchone()[0]
            logging.info("数据库的结果为：{}".format(result))
            self.assertEqual(username,result)

        # 断言
        assert_common(self, response, http_code, success, code, message)



    @parameterized.expand(utils.read_delete_emp_json())
    def test04_delete_emp(self, http_code, success, code, message):
        """测试删除员工的方法"""
        response = self.emp_api.delete_emp()
        # 获取修改员工的json数据
        jsonData = response.json()
        # 输出数据
        logging.info("删除员工接口返回的数据为：{}".format(jsonData))
        # 断言
        assert_common(self, response, http_code, success, code, message)

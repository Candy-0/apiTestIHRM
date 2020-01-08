import json

import pymysql

import app


def assert_common(self, response, http_code, success, code, message):
    """通用断言函数"""

    self.assertEqual(http_code, response.status_code)  # 断言响应状态码
    self.assertEqual(success, response.json().get("success"))  # 断言json响应数据中的success
    self.assertEqual(code, response.json().get("code"))  # 断言json响应数据中的code
    self.assertIn(message, response.json().get("message"))  # 断言json响应数据中的message


def read_login_data():
    """读取登录的json数据"""
    data_path = app.BASE_DIR + "/data/login_data.json"
    with open(data_path, "r", encoding="utf-8") as f:
        jsonData = json.load(f)

        # 遍历json中的数据并保存到列表中
        p_list = list()
        for data in jsonData:
            p_list.append((
                data.get("mobile"),
                data.get("password"),
                data.get("http_code"),
                data.get("success"),
                data.get("code"),
                data.get("message")
            ))

        # print(p_list)
        return p_list


def read_add_emp_json():
    """读取员工模块的json数据"""
    file_path = app.BASE_DIR + "/data/employee.json"
    with open(file_path, encoding="utf-8") as f:
        jsonData = json.load(f)
        add_e_list = list()
        for data in jsonData:
            if data == "add_emp":
                add_e_list.append((
                    jsonData.get(data).get("username"),
                    jsonData.get(data).get("mobile"),
                    jsonData.get(data).get("http_code"),
                    jsonData.get(data).get("success"),
                    jsonData.get(data).get("code"),
                    jsonData.get(data).get("message")

                ))
                break
        print(add_e_list)
        return add_e_list


def read_query_emp_json():
    """读取员工模块的json数据"""
    file_path = app.BASE_DIR + "/data/employee.json"
    with open(file_path, encoding="utf-8") as f:
        jsonData = json.load(f)
        query_e_list = list()
        for data in jsonData:
            if data == "query_emp":
                query_e_list.append((
                    jsonData.get(data).get("http_code"),
                    jsonData.get(data).get("success"),
                    jsonData.get(data).get("code"),
                    jsonData.get(data).get("message")

                ))
                break
        print(query_e_list)
        return query_e_list


def read_update_emp_json():
    """读取员工模块的json数据"""
    file_path = app.BASE_DIR + "/data/employee.json"
    with open(file_path, encoding="utf-8") as f:
        jsonData = json.load(f)
        update_e_list = list()
        for data in jsonData:
            if data == "update_emp":
                update_e_list.append((
                    jsonData.get(data).get("username"),
                    jsonData.get(data).get("http_code"),
                    jsonData.get(data).get("success"),
                    jsonData.get(data).get("code"),
                    jsonData.get(data).get("message")
                ))
                break
        print(update_e_list)
        return update_e_list


def read_delete_emp_json():
    """读取员工模块的json数据"""
    file_path = app.BASE_DIR + "/data/employee.json"
    with open(file_path, encoding="utf-8") as f:
        jsonData = json.load(f)
        delete_e_list = list()
        for data in jsonData:
            if data == "query_emp":
                delete_e_list.append((
                    jsonData.get(data).get("http_code"),
                    jsonData.get(data).get("success"),
                    jsonData.get(data).get("code"),
                    jsonData.get(data).get("message")

                ))
                break
        print(delete_e_list)
        return delete_e_list


class DBUtils:
    def __init__(self,host="182.92.81.159",
                 username = "readuser",
                 password= "iHRM_user_2019",
                 database= "ihrm"):
        self.host = host
        self.username = username
        self.password = password
        self.database = database
    # __enter__和__exit__是一对魔法方法，和with结合使用，当执行with时就会自动执行
    # __enter__里面的语句，当with缩进里面的语句执行完以后，就会执行__exit__里面的语句
    def __enter__(self):
        self.conn = pymysql.connect(self.host,self.username,self.password,self.database)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor:
            self.cursor.close()

        if self.conn:
            self.conn.close()





if __name__ == '__main__':
    # main函数的作用
    # 防止调用这个模板或者类时，自动执行代码
    read_login_data()
    read_add_emp_json()
    read_query_emp_json()
    read_update_emp_json()


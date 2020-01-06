import requests
import app


class EmpAPI:

    def __init__(self):
        self.emp_url = app.HOST + "/api/sys/user"
        # 注意：如果我们调调用员工管理模块的相关接口是，先调用login.py接口
        # 获取到的app.HEADERS才会是{"Content-Type":"application/json","Authorization":"Bearer xxxx-xxxx-xxx-xxx"}

        self.headers = app.HEADERS

    def add_emp(self,username,mobile):
        """添加员工接口"""
        data = {"username": username,
                "mobile": mobile,
                "timeOfEntry": "2020-01-01",
                "formOfEmployment": 1,
                "worknumber":"1234",
                "departmentName": "测试",
                "departmentId": "1210411411066695680",
                "correctionTime": "2020-01-02T16:00:00.000Z"}
        # 发送添加员工接口请求
        response = requests.post(self.emp_url,json=data,headers=self.headers)
        # 返回添加员工接口的响应数据
        return response

    def query_emp(self):
        """查询员工接口"""
        url = self.emp_url + "/" + app.EMP_ID
        return requests.get(url,headers = self.headers)

    def update_emp(self,username):
        """修改员工接口"""
        url = self.emp_url + "/" + app.EMP_ID
        data = {"username":username}
        return requests.put(url,json=data,headers = self.headers)

    def delete_emp(self):
        """删除员工接口"""
        url = self.emp_url + "/" + app.EMP_ID
        return requests.delete(url,headers=self.headers)

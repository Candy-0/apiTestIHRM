import requests
import app


class LoginAPI:
    """登录接口类"""

    def __init__(self):
        self.login_url = app.HOST + "/api/sys/login"  # 登录url
        self.headers = app.HEADERS

    def get_login_url(self, mobile, password):
        """获取登录接口方法"""
        # 这里使用两个变量来接收字典数据，是为了方便后续进行参数化处理
        data = {"mobile": mobile, "password": password}
        # 发送登录请求
        response = requests.post(self.login_url,
                                json=data,
                                headers=self.headers)
        # 返回响应数据
        return response

import app
import logging

# 初始化日志
"""为什么要在api.init文件中初始化日志呢？
因为我们在后面进行接口测试是，都会调用封装的API接口，调用时，
会自动运行__init__.py函数，将日志的调用文件放在这里，从而实现初始化日志器的功能"""

app.init_login()

# logging.info("kkkkkk")
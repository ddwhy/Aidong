import requests

from MDX.apiFrame.apiFrame.api.loginApi import MtxLogin


class TestLogin:
    def setup_class(self):
        self.session = requests.Session()
        # 实例化接口对象
        self.login_obj = MtxLogin()

    def test_login_success(self):
        data = {'accounts':'yaoyao','pwd':'yaoyao'}
        resp_login = self.login_obj.login(self.session,data)
        assert resp_login.json().get('msg') == "登录成功"

    # 参数化  用yml文件去保存我们的测试数据
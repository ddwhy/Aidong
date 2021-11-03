import pytest
import allure
import requests
from MDX.apiFrame.apiFrame.api.loginApi import MtxLogin
from MDX.apiFrame.apiFrame.tools.analyze_data import analyze_data

class TestLogin:
    def setup_class(self):
        self.session = requests.Session()
        # 实例化接口对象
        self.login_obj = MtxLogin()

    # 测试登录成功的测试用例
    @allure.story('登录成功的测试用例')
    def test_login_success(self):
        '''
        登录成功的测试用例
        :return:
        '''
        resp_login = self.login_obj.login_success(self.session)
        assert resp_login.json().get('msg') == "登录成功"

    # 参数化  用yml文件去保存我们的测试数据
    # data_list = [{},{},{},{}]  for dict in data_list:
    @pytest.mark.parametrize('args', analyze_data('login_data','test_login'))
    @allure.title('登录异常，测试数据是:{args}')
    @allure.story('异常数据的登录接口测试')
    def test_login_error(self, args):
        '''
        对登录接口进行异常登录的测试
        :param args: 参数化的数据
        :return:
        '''
        data = {'accounts':args['accounts'], 'pwd': args['pwd']}
        resp_login = self.login_obj.login(self.session, data)
        assert resp_login.json().get('msg') == args['exp']
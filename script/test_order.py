import requests

from MDX.apiFrame.apiFrame.api.orderApi import Order
from MDX.apiFrame.apiFrame.api.loginApi import MtxLogin
import allure

class TestOrder:
    def setup_class(self):
        # web ui自动化 创建driver
        # 初始化操作---每条测试用例之前要进行的操作
        self.session = requests.Session()
        self.order_obj = Order()
        # 调用成功的登录接口
        MtxLogin().login_success(self.session)

    @allure.story('提交订单接口的测试')
    @allure.title('提交订单接口测试用例')
    def test_order(self):
        '''
        依赖于登录：api级别的，请求级别，完全独立
        :return:
        '''
        # 调用成功的登录接口
        # MtxLogin().login_success(self.session)
        resp_order = self.order_obj.order(self.session)
        assert resp_order.json().get('msg') == "提交成功"


    def test_order_error(self):
        # 调用成功的登录接口
        # MtxLogin().login_success(self.session)
        pass

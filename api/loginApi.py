'''
   ip = 'http://121.42.15.146:9090'
    headers = {'X-Requested-With':'XMLHttpRequest'}

    @pytest.mark.parametrize("accouts,pwd,exp", data_li,ids=ids)
    def test_login(self,accouts, pwd, exp):
        url_login = self.ip + '/mtx/index.php?s=/index/user/login.html'
'''
from MDX.apiFrame.apiFrame.config  import IP, HEADERS
from MDX.apiFrame.apiFrame.tools.logger import GetLog
import allure
log = GetLog().get_logger()


class MtxLogin(object):
    def __init__(self):
        self.url = IP + '/mtx/index.php?s=/index/user/login.html'
        log.info(f'登录的url地址是{self.url}')

    def login(self, session, data):
        log.info(f'登录的data数据是{data}')
        resp_login = session.post(self.url, data=data, headers=HEADERS)
        log.info(f'登录的响应数据是{resp_login}')
        return resp_login

    def login_success(self,session):
        '''
        发起登录成功的请求
        :param session:
        :return:
        '''
        data = {'accounts': 'yaoyao', 'pwd':'yaoyao'}
        resp_login = session.post(self.url, data=data, headers=HEADERS)
        return resp_login

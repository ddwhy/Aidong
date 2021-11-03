import base64
import hashlib


class Secret(object):
    '''
    实现加密方法
    '''
    def __init__(self,string):
        '''
        需要对字符串进行encode()
        '''
        self._string = string.encode('utf-8')

    def md5(self):
        '''
        md5加密方法
        :return:
        '''
        try:
            sign = hashlib.md5(self._string).hexdigest()
            return sign
        except:
            return False

    def sha1(self):
        '''
        实现sha1的算法封装
        :return:
        '''
        try:
            sign = hashlib.sha1(self._string).hexdigest()
            return sign
        except:
            return False

    def base64encode(self):
        '''
        实现一个base64 编码的方法封装
        :return:
        '''
        try:
             return base64.b64encode(self._string).decode('utf-8')
        except:
            return False


    def base64decode(self):
        '''
        base64 解码的方法封装
        :return:
        '''
        try:
             return base64.b64decode(self._string).decode('utf-8')
        except:
            return False


if __name__ == '__main__':
    str = 'hahaha'
    print(Secret('aGFoYWhh').md5())
    # 解码  对编码之后的字符串进行解码
    print(Secret('aGFoYWhh').base64decode())
    # 编码  对字符串进行编码
    print(Secret(str).base64encode())

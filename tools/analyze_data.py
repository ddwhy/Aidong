import yaml
import MDX.apiFrame.apiFrame.config as config
# import config

def analyze_data(filename,key):
    '''
    解析yml文件，得到一个列表嵌套字典的数据格式
    :param filename: login_data.yml 文件名
    :param key: test_login 键名
    :return: 列表嵌套字典的数据格式
    '''
    with open(config.DIR_NAME + '/data/%s.yml' % filename, 'r', encoding='utf-8') as f:
        print(config.DIR_NAME)
        data_list = list()
        yaml_data = yaml.load(f, Loader=yaml.FullLoader) #读取文件数据
        print(f'yaml_data的值是{yaml_data}')
        pre_value = yaml_data.get(key)
        li = pre_value.values()
        # print(f'li的值是{li}')
        # for value in li:
        #     data_list.append(value)
        data_list.extend(li)    #将列表拼接到另一个列表中extend()，等于append
        return data_list
        # 构造数据---列表套字典
        # [{'accouts':'','pwd':'','exp':''},{'accouts':'','pwd':'','exp':''}]

    # with open('../data/login_data.yml','r',encoding='utf-8') as f:
    #     yaml_data = yaml.load(f,Loader=yaml.FullLoader)
    #     print(yaml_data)

if __name__ == '__main__':
    data_list = analyze_data('login_data', 'test_login')
    print(data_list)
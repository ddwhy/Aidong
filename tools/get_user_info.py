import time
import string
from faker import Faker
import random


def get_user_info(count):
    '''
    获取用户信息
    :return:
    '''
    faker = Faker(locale="zh_CN")
    data_list = []

    for i in range(1, count+1):
        dic = {}
        username = faker.first_name()
        password = faker.password(special_chars=False)
        gender = random.randint(0,1)
        mobile = faker.phone_number()
        email = faker.email()
        address = faker.address()
        id_card = faker.ssn()
        dic['userName'] = username
        dic['password'] = password
        dic['gender'] = gender
        dic['mobile'] = mobile
        dic['email'] = email
        dic['address'] = address
        dic['id_card'] = id_card
        data_list.append(dic)

    return data_list


def get_register_info(count,minlength = 6,maxlength = 16):
    '''
    针对注册手动写的构造假数据的方法（pinter的注册接口为例子）
    :param count:
    :param minlength:
    :param maxlength:
    :return:
    '''
    #{"userName":"test","password":"1234","gender":1,
    # "phoneNum":"110","email":"beihe@163.com","address":"Beijing"}
    data_list = []
    minlength = 6
    maxlength = 16
    mobile_begin_seed = ['134', '135', '136', '137', '138', '139', '150', '151', '152', '157', '158', '159', '182',
                         '183', '187', '188', '130', '131', '132', '155', '156', '175', '185', '186', '133', '153',
                         '177', '180', '181', '189']
    mobile_seed = string.digits  # 0-9的所有数字
    username_seed = string.digits + string.ascii_letters  # a-zA-Z0-9
    password_seed = string.digits + string.ascii_letters   # a-zA-Z0-9加上所有标点符号

    for i in range(1, count+1):
        mobile = random.choice(mobile_begin_seed) + ''.join(random.choice(mobile_seed) for m in range(8))
        username = ''.join(random.choice(username_seed) for u in range(random.randint(minlength, maxlength)))
        password = ''.join(random.choice(password_seed) for p in range(random.randint(minlength, maxlength)))
        gender = random.randint(0, 1)
        data_list.append( {"userName":username,"password":password,"gender":gender,"mobile":mobile,"email":username+"@163.com","address":"Beijing"}
                    )
    return data_list


if __name__ == '__main__':
    print(get_user_info(3))
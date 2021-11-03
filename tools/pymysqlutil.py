import pymysql

class DataBaseHandle(object):
    """定义MYSQL数据库操作类"""
    def __init__(self):
        '''
        实例方法共用的属性
        建立mysql的连接
        '''
        self.ip = '192.168.2.221'
        self.port = 3306
        self.username='root'
        self.password = '123456'
        self.database ='mtx'
        # 建立一个mysql的连接
        self.db =pymysql.connect(self.ip, self.username, self.password,self.database,self.port)

    def insertDB(self, sql):
        """插入数据
        insert into s_user(username,pwd) values("bull",12345)
        """
        # 获取游标
        self.cursor = self.db.cursor()
        try:
            # 执行插入语句
            self.cursor.execute(sql)
            # 对数据进行提交
            self.db.commit()
        except Exception as err:
            print('insert data error:', err)
            self.db.rollback()  # 发生错误时回滚
        finally:
            self.cursor.close()

    def deleteDB(self,sql):
        """删除数据
            delete from s_user where username="mixuhui"
        """
        self.cursor = self.db.cursor()
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as err:
            print('delete data error:',err)
            self.db.rollback()
        finally:
            self.cursor.close()

    def updateDB(self, sql):
        """修改数据 sql
        update s_user set name="yaoyao" where name="shamo"
        """
        self.cursor = self.db.cursor()
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as err:
            print('update data error:',err)
            self.db.rollback()
        finally:
            self.cursor.close()

            # 查询方法

    def selectDb(self, sql):
        '''
        sql语句就是正常的mysql的查询语句 原生的sql
        :param sql:
        :return:
        '''
        # 建立一个‘cursor游标’对象操作数据库
        cur = self.db.cursor()
        # 写sql语句容易出现问题，所以用try...except...finally进行补获
        try:
            # 执行sql语句  用游标进行查询---返回结果---把结果保存在游标里面
            cur.execute(sql)
            # 从游标里面读取数据，赋值给一个变量
            data = cur.fetchall()
            return data

        except Exception as e:
            print(e)
            raise e
        finally:
            # 把游标进行关闭
            cur.close()

    def closeDB(self):
        """关闭数据库连接"""
        self.db.close()


if __name__ == '__main__':
    db = DataBaseHandle()
    data = db.selectDb('select pwd,username from s_user where username = "shamo"')
    print(data)
    db.updateDB('update s_user set username="yaoyao" where username="shamo"')
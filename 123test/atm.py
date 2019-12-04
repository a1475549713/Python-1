import pymysql


class Sql():
    def __init__(self, host='localhost',
                 user='lu',
                 passwd='123456',
                 db='lusql',
                 port=3306):
        self.connert = pymysql.connect(host, user, passwd, db, port)

        self.cursor = self.connert.cursor()

    def selects(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def inserts(self, table, data):
        # data = [('eee', '123456')]
        sql = "insert into {} values (%s,%s)".format(table)
        self.cursor.executemany(sql, data)
        self.connert.commit()


if __name__ == '__main__':
    mysql = Sql()
    usename = input('用户名：')
    pwd = input('密码：')
    try:
        sql = "select name from atmuse where pwd='{}'".format(pwd)
        # print(sql)
        if len(mysql.selects(sql)) == 0:
            data = [(usename, pwd)]
            # print(data)
            mysql.inserts(table='atmuse(name,pwd)', data=data)
            print('注册成功')
        else:
            if mysql.selects(sql) == (usename,):
                print("登录成功")

            else:
                print("密码错误")
    except TypeError:
        pass

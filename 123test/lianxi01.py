import pymysql
import sys


class My_Sql():
    def __init__(self, host='localhost', user='lu', passwd='123456', db='sql01', port=3306):
        self.connert = pymysql.connect(host, user, passwd, db, port)
        self.cursor = self.connert.cursor()

    def selects(self, sql):
        self.cursor.execute(sql)  # 找到的数据总和
        # print(self.cursor.fetchone())
        return self.cursor.fetchone()

    def inserts(self, sql, data):
        self.cursor.executemany(sql, data)
        self.connert.commit()
        return True

    def deletes(self, sql):
        self.cursor.execute(sql)
        self.connert.commit()


class Atm(My_Sql):
    def __init__(self, user, pwd):
        super(Atm, self).__init__()
        self.user = user
        self.pwd = pwd

    def check(self, use):
        sql = 'select pwd from username  where card="{}"'.format(use)
        s = self.selects(sql)
        if s != None:
            return s
        else:
            return False

    def login(self):  # 登陆
        n = 1
        while True:
            if self.check(self.user) == (self.pwd,):
                print('登陆成功')
                return True
            else:
                n += 1
                if n < 4:
                    print('密码错误')
                    self.pwd = int(input('重新输入密码：'))
                else:
                    print('密码错误三次，退出')
                    sys.exit()

    def login_in(self):  # 注册
        data = [(self.user, self.pwd)]
        sql = 'insert into username(card,pwd) values (%s,%s)'
        self.inserts(sql, data)
        sql = 'insert into deposit(card) values (%s)'
        self.inserts(sql, [(self.user)])
        print('注册成功')

    def checkbalance(self):  # 查余额
        sql = "select money from deposit where card= '{}'".format(self.user)
        return self.selects(sql)[0]   #?

    def modifybalance(self, add, user):  # 存/取
        sql = "update deposit set money ={} where card= '{}'".format(add, user)
        self.deletes(sql)

    def deposit(self, add):  # 要修改的余额
        new = self.checkbalance() + add
        return new

    def delete(self):  # 删
        sql = "delete deposit, username from deposit left join username on deposit.card =username.card where deposit.card= '{}'".format(
            self.user)
        self.deletes(sql)
        print('删除成功')


if __name__ == '__main__':
    use = input('账号：')
    pswd = int(input('密码：'))
    atm = Atm(use, pswd)
    if not atm.check(use):
        atm.login_in()
    while True:
        check = input('1：存，2：取，3：转，4：销，5：退出')#/n
        if check == "1":
            add = int(input('输入存款金额：'))
            if add < 0:
                print('输入正确金额')
            else:
                atm.modifybalance(atm.deposit(add), use)
                print("存款{}成功,当前账户余额{}".format(add, atm.checkbalance()))
        elif check == "2":
            add = int(input('输入取款金额：'))
            if add <= 0:
                print('输入正确金额')
            elif add > atm.checkbalance():
                print('余额不足')
            else:
                atm.modifybalance(atm.deposit(add * -1), use)
                print("取款{}成功,当前账户余额{}".format(add, atm.checkbalance()))
        elif check == "3":
            a = input('输入收款账户')
            if atm.check(a):
                while True:
                    add = int(input('输入转账金额：'))
                    if add == 0:
                        print('退出转账')
                        break
                    elif add < 0:
                        print('输入正确金额')
                    elif add > atm.checkbalance():
                        print('余额不足,重新输入,退出按0')
                    else:
                        atm.modifybalance(atm.deposit(add * -1), use)
                        atm.modifybalance(atm.deposit(add), a)
                        print("转账{}成功,当前账户余额{}".format(add, atm.checkbalance()))
            else:
                print('账号{}不存在'.format(a))
        elif check == "4":
            atm.delete()
            sys.exit()
        elif check == "5":
            sys.exit()
        else:
            print('请正确选择')
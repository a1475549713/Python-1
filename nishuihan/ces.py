from multiprocessing import Process

from time import sleep


def A():
    for i in range(100):
        with open("11.txt", 'a') as  f:
            f.write(str(i) + "\r\n")
            sleep(1)


def B():
    for i in range(300, 500):
        with open("11.txt", 'a') as  f:
            f.write(str(i) + "\r\n")
            sleep(1)


def AA():
    for i in range(1, 10):
        yield i


import win32com.client

dm = win32com.client.Dispatch('dm.dmsoft')
Tu_Ku = dm.SetPath(r'C:\Users\Administrator\Desktop\wenjian\图文件')


def Zhao_Tu(x1, y1, x2, y2, file, color="36.2.87-180.5.60"):
    return dm.FindPic(x1, y1, x2, y2, file, color, 0.8, 0)

# import time
# # z = Zhao_Tu(61, 110, 658, 335, '与xxx对话.bmp|')
# g = dm.Reg("2244939288cfa31e5135147e45e56bbc65440c5b8c", "")
# #bd = dm.BindWindowEx(197968, 'dx2', 'dx2', 'dx', 'dx.public.disable.window.size', 101)
# dm_ret = dm.CapturePng(0,0,2000,2000,r"C:\Users\Administrator\Desktop\wenjian\{}.png".format(time.time()))
# print(dm_ret)

def p1():
    sleep(5)
    print("p1")
    sleep(5)
def p2():
    sleep(5)
    print("p2")
    sleep(5)

def maopao(list):
    while True:
        N=0
        for i in range(0,len(list)-1):
            if list[i]>list[i+1]:
                list[i],list[i+1]=list[i+1],list[i]
                N+=1
        if N==0:
            print(list)
            break

import requests
# url= "https://mail.163.com/js6/main.jsp?sid=YArywnPqJdcyrOSWcYqqAFwVAAzSsKGC&df=mail163_letter HTTP/1.1"
# header={
# "Host": "mail.163.com",
# "Connection": "keep-alive",
# "Upgrade-Insecure-Requests":"1",
# "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
# "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
# "Accept-Encoding": "gzip, deflate, br",
# "Accept-Language": "zh-CN,zh;q=0.9",
# }
# Cookie= "mail_health_check_time=1562340696615; starttime=; mail_upx_nf=; mail_idc=; MAIL_MISC=v993611; secu_info=1; locale=; mail_style=js6; mail_uid=v993611@163.com; mail_host=mail.163.com; _ntes_nnid=dc07cb3ad59077263764f764272dc929,1562340697198; _ntes_nuid=dc07cb3ad59077263764f764272dc929; NNSSPID=ada4da9e98854c7c93fc9e3a11dfd2b8; Coremail.sid=pBFUyTahZbrWMuJTIzhhspgeniShOEIQ; _autoLogin=1562340866836%7C1; NTES_SESS=lZpnNO1YsuuuFS1.WjLxGUDs_Bh._1ajMTimYDA4sJsKQkujQqfOaEgEbpfi7A7N2S.AYVXnaznzBD7nyPfo5jhFA5Et_pB3gh6rKkyirZXNVc28PslYzGwBojA.1Mv5WvGkK9iEJ5kY7kcZdK7rhhKcM9OpTAk3hO1DRr6rUXH_8bGEeC2IAFAD6O2Wen9DYtaeXLnlffyMfiGlROJAz_jyY; S_INFO=1562340877|0|2&70##|v993611; P_INFO=v993611@163.com|1562340877|0|mail163|00&12|zhj&1562333336&nsh#zhj&330100#10#0#0|177258&0|mail163&nsh_qrcode|v993611@163.com; df=mail163_letter; mail_upx=t2bj.mail.163.com|t3bj.mail.163.com|t4bj.mail.163.com|t1bj.mail.163.com; Coremail=678beef590744%YArywnPqJdcyrOSWcYqqAFwVAAzSsKGC%g3a22.mail.163.com; cm_last_info=dT12OTkzNjExJTQwMTYzLmNvbSZkPWh0dHBzJTNBJTJGJTJGbWFpbC4xNjMuY29tJTJGanM2JTJGbWFpbi5qc3AlM0ZzaWQlM0RZQXJ5d25QcUpkY3lyT1NXY1lxcUFGd1ZBQXpTc0tHQyZzPVlBcnl3blBxSmRjeXJPU1djWXFxQUZ3VkFBelNzS0dDJmg9aHR0cHMlM0ElMkYlMkZtYWlsLjE2My5jb20lMkZqczYlMkZtYWluLmpzcCUzRnNpZCUzRFlBcnl3blBxSmRjeXJPU1djWXFxQUZ3VkFBelNzS0dDJnc9aHR0cHMlM0ElMkYlMkZtYWlsLjE2My5jb20mbD0tMSZ0PS0xJmFzPXRydWU=; MAIL_SESS=lZpnNO1YsuuuFS1.WjLxGUDs_Bh._1ajMTimYDA4sJsKQkujQqfOaEgEbpfi7A7N2S.AYVXnaznzBD7nyPfo5jhFA5Et_pB3gh6rKkyirZXNVc28PslYzGwBojA.1Mv5WvGkK9iEJ5kY7kcZdK7rhhKcM9OpTAk3hO1DRr6rUXH_8bGEeC2IAFAD6O2Wen9DYtaeXLnlffyMfiGlROJAz_jyY; MAIL_SINFO=1562340877|0|2&70##|v993611; MAIL_PINFO=v993611@163.com|1562340877|0|mail163|00&12|zhj&1562333336&nsh#zhj&330100#10#0#0|177258&0|mail163&nsh_qrcode|v993611@163.com; mail_entry_sess=1f2d060894866167b79d256880e0e806815c3434ad4b702b597b7b963b96dca43a006932c7f18907c89cf4a858f704d55c50499ae3b87c52e068db8f492758738bfd813ef5736bafea23fc4f1c40b6962f14e75a55ac0cbf74847a64618f36f88a9b5b2fcb35d64a31efd087ac1eaf3817b8418f1c144e9c037b0a252d551030c68c714221abb0ed8c617b2a3fe9c3fc127a4ed3b5e0081b5ae1c4bcea0c1029aa320a0a5141bda6ac389d8da88c155e720c65c0c45302e4db465d3e35cfbd3e; JSESSIONID=838737A1B4344B95AC06F6AB9897DA38"
# cookie = {}
# for i in Cookie.split(';'):
#         key = i.split("=")[0]
#         var = i.split("=")[1]
#         cookie[key] = var
#
# rsp=requests.get(url,headers=header,cookies=cookie,verify=False)
# print(rsp.cookies)


url = "https://mail.163.com/entry/cgi/ntesdoor?"
header={
"Host": "mail.163.com",
"Connection": "keep-alive",
"Content-Length": "0",
"Cache-Control": "max-age=0",
"Origin": "https://email.163.com",
"Upgrade-Insecure-Requests": "1",
"Content-Type": "application/x-www-form-urlencoded",
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
"Referer": "https://email.163.com/",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "zh-CN,zh;q=0.9"
}
data = "t=1&language=-1&iframe=1&product=mail163&from=web&df=email163&module=&style=-1&allssl=true&CH=1&url2=http://email.163.com/errorpage/error163.htm"
data = data.split("&")
data1={}
for i in data:
    key = i.split("=")[0]
    val = i.split("=")[1]
    data1[key] = val
import json
cooks = "starttime=;NTES_SESS=k38dwtfmbdf0JpSR4apywNFqbxQ0fTxvkJ6xzW8IUhU_7LHE7Muc9bTbwqu6d8dPjpr8zasv9KvKQWdv2YuXyEN58ybStqQ.TfxjEIS7tPKBa0y3mXYbJ8IQXE8renCygCDL_B6bhyL2pUtyKjrkAdmy7DjJtU.ceQ4LKh6Qse6ZFN0GXpmU4m1JorZ8jQhFFjGyvQcgpDL7u6Dkich8KtE2z&S_INFO=1562374690|0|2@70##|v993611;P_INFO=v993611@163.com|1562374690|0|mail163|00&12|zhj&1562342722&mail163#zhj&330100#10#0#0|177258&0|mail163&nsh_qrcode|v993611@163.com;df=mail163_letter"
cook1={}
for i in cooks.split(";"):

    key = i.split("=")[0]
    val = i.split("=")[1]
    cook1[key] = val

rsp1 =requests.post(url,headers=header,verify=False,data=data1,cookies = cook1)

print(rsp1.headers)
print(requests.utils.dict_from_cookiejar(rsp1.cookies))
print(rsp1.text)






if __name__ == '__main__':
    pass
    # l = [3, 5, 2,1,0,15,23,0]
    # maopao(l)
    # p = []
    # p.append(Process(target=p1,))
    # p.append(Process(target=p2,))
    # for i in p:
    #     # i.daemon=True
    #     i.start()
    #     # i.join()
    # # r1 =Process(target=p1,)
    # # r1.start()
    # print("end")



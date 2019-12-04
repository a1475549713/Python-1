from suds.client import Client
from suds.xsd.doctor import ImportDoctor, Import
import requests
import json
import pytest
import datetime

url = "http://www.webxml.com.cn/WebServices/IpAddressSearchWebService.asmx?wsdl"

imp = Import('http://www.w3.org/2001/XMLSchema', location='http://www.w3.org/2001/XMLSchema.xsd')

imp.filter.add('http://WebXml.com.cn')

# doctor = ImportDoctor(imp)
# client = Client(url,doctor=doctor)
# print(client.service.getCountryCityByIp("117.28.35.18"))
# rsp = requests.get(url)

# print(rsp.text)

data = '''
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:web="http://WebXml.com.cn/">
   <soapenv:Header/>
   <soapenv:Body>
      <web:getCountryCityByIp>
         <!--Optional:-->
         <web:theIpAddress>117.75.179.13</web:theIpAddress>
      </web:getCountryCityByIp>
   </soapenv:Body>
</soapenv:Envelope>'''

# rsp = requests.post(url=url,data=data.encode("utf-8"))
# print(rsp.text)


'''
data = ["13588620187","135886236187","13188620187"]
@pytest.fixture(params=data,scope="module")
def getuse(request):
    data = request.param
    url1 ="https://tcc.taobao.com/cc/json/mobile_tel_segment.htm?tel={}".format(data)
#data1 = json.dumps(data1)
    session = requests.Session()
    rsp = session.get(url = url1)

    yield rsp
    with open('1.txt','a') as f:
        f.write(rsp.text)

def test_case(getuse):
    assert "mts" in getuse.text ,"mts 不存在"
def test_case1(getuse):
    assert getuse.status_code ==200 ,"访问失败"
def test_case2(getuse):
    assert "province" in getuse.text, "province 不存在"
def test_case3(getuse):
    assert "catName" in getuse.text, "catName 不存在"


if __name__ == '__main__':
    pytest.main(["C:/Users/Administrator/PycharmProjects/untitled/123test/lianxi02.py"])
'''
import itertools


def A(l):
    for i in l:
        if i % 2 == 0:
            yield i


l = [1, 2, 3, 4, 5, 6, 7, 9]
l1 = [1, 2, 3, 4, 5, 6, 7, 9]


def B(l):
    n = 0
    for i in A(l):
        n += i
    return n


# print(B(l))
z = sum(i for i in l if i % 2 == 0)
# print(z)

for a, b in itertools.product(l, l1):
    if a + b == 10:
        pass
        #print(a, b)
#    print(a,b)
for i in itertools.islice(l,0,None,2):
    print(i)

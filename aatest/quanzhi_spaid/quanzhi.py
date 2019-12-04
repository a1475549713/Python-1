import requests
from lxml import etree
import random



def get_responce(url,header):
    rsp = requests.get(url,headers=header)
    rsp.encoding = "gbk"
    # print(html.text)
    html = etree.HTML(rsp.text)
    get_body(html)


def get_body(html):
    name = html.xpath('//div[@class="box_con"]/div[@id="list"]/dl/dd/a')
    for i in name:
        title = i.xpath('./text()')[0].strip("?")
        href = i.xpath('./@href')[0]
        #print(title ,href,)
        get_book(url,href,title)

def get_book(url,href,title):

    url = url + href
    body =requests.get(url)
    body.encoding="gbk"
    html = etree.HTML(body.text)
    book = html.xpath("//div[@class='content_read']/div/div[@id='content']/text()")
    book = "".join(book).replace(u"\xa0\xa0\xa0\xa0","\r\n")
    #print(book)
    with open("./全职法师/'{}".format(title),'w',encoding='gbk') as f:
        f.write(book)
        #pass


if __name__ == '__main__':
    url = "https://www.booktxt.net/0_595/"
    UseAgent = ['Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36',
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60",
                "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
                "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16"]
    header = {
        'Use-Agent':random.choices(UseAgent)[0],
        'Referer':url
    }

    get_responce(url,header)
import requests, time, random
from lxml import etree
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
def spider():
    headers = {
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3664.3 Safari/537.36',
               'accept-language': 'zh-CN,zh;q=0.9',
                'accept-encoding': 'gzip, deflate, br',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'cookie': '_ga=GA1.3.1015902756.1548838099; qchatid=1c98cab4-15a9-4b86-96f7-d6f3c28873d5; WINDOW_DEVICE_PIXEL_RATIO=1.25; CITY_NAME=SHENZHEN; RENTROOMREADRECORDCOOKIE=100457223; ROOM_SALE=%2Fsale%2Fb3%5E%20%E4%B8%89%E5%AE%A4; SALEROOMREADRECORDCOOKIE=100456330; looks=SALE%2C100456330%2C58704; cookieId=5ce29f45-2f0f-4c70-8032-ab797ae7bca1; acw_tc=3afa7f9615517105316324442e396d129300bd29a4f93426aceac81482; sid=d1cdc853-31db-480c-8b1a-e2e488c97e88; _jzqckmp=1; _gid=GA1.3.268753963.1551710536; sec_tc=AQAAAL7mg01i0wEAGypZoG2lb23T/K1r; acw_sc__v2=5c7dc82e05abce18e25bd1d06f0c524085c9a8cd; JSESSIONID=aaavHpwSXdZ6M_CUFvlLw; Hm_lvt_de678bd934b065f76f05705d4e7b662c=1549966254,1550021752,1551710536,1551747122; Hm_lpvt_de678bd934b065f76f05705d4e7b662c=1551747122; _dc_gtm_UA-47416713-1=1; _qzja=1.799695471.1548923388318.1551710536503.1551747122388.1551715556774.1551747122388.0.0.0.50.11; _qzjc=1; _qzjto=5.1.0; _jzqa=1.2794576650160789000.1548923387.1551710536.1551747123.11; _jzqc=1; _jzqx=1.1548923387.1551747123.8.jzqsr=shenzhen%2Eqfang%2Ecom|jzqct=/rent/100457223.jzqsr=shenzhen%2Eqfang%2Ecom|jzqct=/sale/f1; _qzjb=1.1551747122388.1.0.0.0; _jzqb=1.1.10.1551747123.1'
                }
    #print("#####")
    pre_url = 'https://shenzhen.qfang.com/sale/f'
    proxies = {"http": "116.209.59.225	9999"} #免费代理ip地址 https://www.xicidaili.com/nn/
    request = requests.session()
    timeout = random.choice(range(80, 180))  # 超时时间
    for x in range(1, 5):
        html = request.get(pre_url+str(x), headers=headers, timeout=timeout, verify=False, proxies=proxies)
        time.sleep(1)
        html.encoding = 'utf-8'
        code = html.status_code  # 返回状态,200代表OK
        print(code)
        #用获取的页面初始化etree，得到一个delector，然后在这个selector上使用XPath提取数据
        selector = etree.HTML(html.text)
        #print("******", selector)

        house_list = selector.xpath('//*[@id="cycleListings"]/ul/li')
        for house in house_list:
            apartment = house.xpath('./div[1]/p[1]/a/text()')[0].split(' ', 1)[0]
            xiangq = house.xpath('./div[1]/p[1]/a/text()')[0].split(' ', 1)[1]
            house_layout = house.xpath('./div[1]/p[2]/span[2]/text()')[0]
            area = house.xpath('./div[1]/p[2]/span[4]/text()')[0]
            decotored = house.xpath('./div[1]/p[2]/span[6]/text()')[0]
            louceng = house.xpath('./div[1]/p[2]/span[8]/text()')[0].strip()
            chaoxiang = house.xpath('./div[1]/p[2]/span[10]/text()')[0]
            total = house.xpath('./div[2]/span[1]/text()')[0]
            total_price = house.xpath('./div[2]/p/text()')[0]
            item = [apartment, house_layout, area, decotored, louceng, chaoxiang, total_price, total, xiangq]
            #data_writer(item)
            print("正在爬取", apartment, house_layout, area, chaoxiang, decotored, louceng, total_price, total, xiangq)  # 编辑器里打开显示爬取

if __name__ == '__main__':
    spider()
    print("haha! meifen is a big fool!")


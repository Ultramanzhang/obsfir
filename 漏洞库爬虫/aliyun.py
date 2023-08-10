import csv
import time
import requests
from lxml import etree
import re
import io
import sys
from urllib.parse import urljoin

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  # 改变标准输出的默认编码

"""
@author: zhegu、平芜尽处外
@version：0.2
"""


class Aliyun():

    # 初始化函数，防止一些静态参数
    def __init__(self):
        self.pattern = r'title="(.*?)"'

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183'
        }
        self.url = "https://avd.aliyun.com/search"  # 阿里云漏洞库的搜索地址
        self.pagrams = {}  # 搜索需要用到的参数，暂且定义为空，后续有函数让其改变
        # 以下是存入爬取到的数据
        self.ids = []
        self.urls = []
        self.titles = []
        self.types = []
        self.times = []
        self.status = []

    # 获取请求函数
    def get_HTML(self):
        response = requests.get(url=self.url, params=self.pagrams, headers=self.headers)
        return response

    # 获取页面数量
    def get_page_num(self):
        text = self.get_HTML().text
        tree = etree.HTML(text)
        # 获取页面底部的页码数据
        pages = tree.xpath("/html/body/main/div[2]/div/div[3]/span/text()")
        p = re.compile(r"\d+")
        # 通过正则表达式进行提取
        num = p.findall(pages[0])[1]
        return num

    # 获取所有页面的数据
    def get_data(self):
        page_num = self.get_page_num()
        print("共{}页".format(page_num), flush=True)
        for i in range(int(page_num) + 1):
            print("[*] 正在爬取第{}页".format(i), flush=True)
            self.pagrams["page"] = i
            text = self.get_HTML().text
            self.parse(text)
            time.sleep(2)

    # 解析函数，解析阿里云漏洞库的网页
    def parse(self, text):
        # text = self.get_HTML().text
        # 引入xpath的解析对象
        tree = etree.HTML(text)
        # 提取编号
        ids = tree.xpath('//tr/td[1]/a/text()')
        # 提取标题
        titles = tree.xpath('//tr/td[2]/text()')
        # 提取类型
        types = tree.xpath('//tr/td[3]/button/text()')
        # 提取时间
        times = tree.xpath('//tr/td[4]/text()')
        # 提取状态
        buttun = tree.xpath('//tr/td[5]/button[2]')
        status = []
        for bu in buttun:
            status.append(bu.get('title', ''))

        # 数据清洗，去除爬下来的数据中的空格和换行
        self.ids += [element.strip() for element in ids]
        self.urls += [urljoin(self.url, "/detail?id=" + element.strip()) for element in ids]
        self.titles += [element.strip() for element in titles]
        self.types += [element.strip() for element in types]
        self.times += [element.strip() for element in times]
        self.status += [element.strip() for element in status]

    def input_consumer(self):
        self.pagrams = {
            "q": input("请输入待检测的组件名称：")
        }
        self.get_data()

    # 保存到csv文件中
    def save(self, lists, filename):
        # csv文件的表头
        header = ["AVD编号", "漏洞详情页连接", "漏洞名称", "漏洞类型", "披露时间", "漏洞状态"]
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            # 这个具体实现是chatGpt写的，将5个list的同下标数据写于一行
            writer.writerows(zip(*lists))
        print("内容保存在" + filename + "中")

    # 方便后续的调用，在这里定义一个主函数
    def main(self):
        # 提示用户输入
        self.input_consumer()
        # 执行保存函数
        self.save([self.ids, self.urls, self.titles, self.types, self.times, self.status], "result.csv")


if __name__ == '__main__':
    # 将class实例化
    aliyun = Aliyun()
    # 调用函数主程序
    aliyun.main()

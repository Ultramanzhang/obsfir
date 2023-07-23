import csv
import requests
from lxml import etree

"""
@author: zhegu
@version：0.1
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
        self.titles = []
        self.types = []
        self.times = []
        self.status = []
        #

    # 获取请求函数
    def get_HTML(self):
        response = requests.get(url=self.url, params=self.pagrams, headers=self.headers)
        return response

    # 解析函数，解析阿里云漏洞库的网页
    def parse(self):
        text = self.get_HTML().text
        # 引入xpath的解析对象
        tree = etree.HTML(text)
        # 提取编号
        self.ids = tree.xpath('//tr/td[1]/a/text()')
        # 提取标题
        self.titles = tree.xpath('//tr/td[2]/text()')
        # 提取类型
        self.types = tree.xpath('//tr/td[3]/button/text()')
        # 提取时间
        self.times = tree.xpath('//tr/td[4]/text()')
        # 提取状态
        buttun = tree.xpath('//tr/td[5]/button[2]')
        for bu in buttun:
            self.status.append(bu.get('title', ''))


        # 数据清洗，去除爬下来的数据中的空格和换行
        self.ids = [element.strip() for element in self.ids]
        self.titles = [element.strip() for element in self.titles]
        self.types = [element.strip() for element in self.types]
        self.times = [element.strip() for element in self.times]
        self.status = [element.strip() for element in self.status]

    def input_consumer(self):
        self.pagrams = {
            "q": input("请输入待检测的组件名称：")
        }
        self.parse()

    # 保存到csv文件中
    def save(self, lists, filename):
        # csv文件的表头
        header = ["AVD编号", "漏洞名称", "漏洞类型", "披露时间", "漏洞状态"]
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            # 这个具体实现是chatGpt写的，将5个list的同下标数据写于一行
            writer.writerows(zip(*lists))
        print("内容保存在"+filename+"中")

    # 方便后续的调用，在这里定义一个主函数
    def main(self):
        # 提示用户输入
        self.input_consumer()
        # 执行保存函数
        self.save([self.ids, self.titles, self.types, self.times, self.status], "result.csv")


if __name__ == '__main__':
    # 将class实例化
    aliyun = Aliyun()
    # 调用函数主程序
    aliyun.main()

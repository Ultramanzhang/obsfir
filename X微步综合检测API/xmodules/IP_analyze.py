# -*- coding: utf-8 -*-
'''
微步在线 IP分析具体实现脚本
'''
import csv
import random
import time

import requests
from xutils import Analyze_constant
from xutils import make_params




class IpAnalyze():
    def __init__(self):
        self.baseurl = "https://api.threatbook.cn/v3/scene/ip_reputation"
        self.header = ["IP地址", "运营商", "国家", "国家代码", "省份", "城市", "威胁类型", "情报来源", "发现时间",
                       "更新时间", "可信度评分"]
        self.save_list = []

    def get_response(self, param):
        time.sleep(random.randfloat(0.5, 1))
        response = requests.get(url=self.baseurl, data=param)
        print(response.json())
        exit()
        return response

    def parse(self, ip):
        rsponse = self.get_response(make_params.main(ip))
        json = rsponse.json()
        if json['response_code'] == 0:
            # 处理其他参数
            self.save_json(json=json)
        else:
            # 从里服务器返回
            print(ip + "-------------" + Analyze_constant.Verbose_Msg(json['verbose_msg']))
            exit()

    def save_json(self, json):
        temp_list = []
        # 提取返回值的IP
        ip = ip_address = next(iter(json["data"]))
        temp_list.append(ip)
        # 提取basic字段
        temp_list.append(json["data"][ip]["basic"]["carrier"])  # 运营商
        temp_list.append(json["data"][ip]["basic"]["location"]["country"])  # 国家
        temp_list.append(json["data"][ip]["basic"]["location"]["country_code"])  # 国家代码
        temp_list.append(json["data"][ip]["basic"]["location"]["province"])  # 省
        temp_list.append(json["data"][ip]["basic"]["location"]["city"])  # 城市
        temp_list.append(Analyze_constant.judgments(json["data"][ip]["judgments"]))  # judgments
        # 提取intelligences
        temp_list.append(json["data"][ip]["intelligences"]["threatbook_lab"]["source"])  # 情报来源
        temp_list.append(json["data"][ip]["intelligences"]["threatbook_lab"]["find_time"])  # 发现时间
        temp_list.append(json["data"][ip]["intelligences"]["threatbook_lab"]["update_time"])  # 更新时间
        temp_list.append(json["data"][ip]["intelligences"]["threatbook_lab"]["confidence"])  # 可信度评分
        self.save_list.append(temp_list)

    # 主函数方便调用
    def main(self,ip):
        for i in ip:
            self.parse(i)
        with open(os.path.join(os.path.dirname(__file__), '..', 'output/IP_analyze.csv'), mode='w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(self.header)
            writer.writerows(self.save_list)
        print("结果保存在：output/IP_analyze.csv")

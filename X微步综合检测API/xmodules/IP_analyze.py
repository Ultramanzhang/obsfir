# -*- coding: utf-8 -*-
'''
微步在线 IP分析具体实现脚本
'''
import requests
from ..xutils import make_params
from ..xutils import Analyze_constant


class IpAnalyze():
    def __init__(self):
        self.baseurl = "https://api.threatbook.cn/v3/scene/ip_reputation"

    def get_response(self, param):
        response = requests.get(url=self.baseurl, data=param)
        return response

    def parse(self, ip):
        rsponse = self.get_response(make_params.main(ip))
        json = rsponse.json()
        if json['response_code'] == 0:
            print(Analyze_constant.analyze(0))

        else:
            print(Analyze_constant.analyze(json['response_code']))
            exit()

    # 主函数方便调用
    def main(self, ip):
        for i in ip:
            self.parse(i)

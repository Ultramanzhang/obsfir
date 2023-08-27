'''
微步在线 文件反病毒引擎检测报告
'''
import os
import requests
import json
from ..xutils import make_multiengines_params
from ..xutils import Analyze_constant


class Filemulti():
    def __init__(self):
        self.baseurl = "https://api.threatbook.cn/v3/scene/ip_reputation"

    def get_response(self, query):
        response = requests.get(url=self.baseurl, params=query)
        return response

    def query(self, sha256):
        rsponse = self.get_response(make_multiengines_params.main(sha256))
        json = rsponse.json()
        if json['response_code'] == 0:
            # 处理服务器返回code
            print(Analyze_constant.response_code(0))
            # 处理其他参数
        else:
            # 从里服务器返回
            print(Analyze_constant.Verbose_Msg(json['verbose_msg']))
            exit()

    # 主函数方便调用
    def main(self, file_dir):
        # 读取文件
        tf = open("../xutils/sha256.json", "r")
        # dirs为一个一维数组，包含路径下所有子目录名
        for root, dirs, files in os.walk(file_dir):
            # 遍历文件列表，传递目录下所有文件名和路径（包括子目录）
            for file in files:
                dict = json.load(tf)
                self.query(dict[file])
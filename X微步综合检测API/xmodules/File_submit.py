'''
微步在线 提交文件分析
针对办公终端、Web/FTP/邮件附件等疑似恶意文件，
终端/服务器的可疑文件等，通过 22 款反病毒扫描引擎快速检测，
并根据不同文件类型，系统自动选择可运行的沙箱环境进行动态检测。
'''
import os
import requests

# 处理post请求
from ..xutils import make_post_params
# Analyze_constant用于处理本项目中网页的返回数据对应值
from ..xutils import Analyze_constant


class Filesubmit():
    def __init__(self):
        self.baseurl = "https://api.threatbook.cn/v3/file/upload"

    def post_response(self, file_name, file_dir):
        files = {
            'file': (file_name, open(os.path.join(file_dir, file_name), 'rb'))
        }
        # 发送post请求
        response = requests.post(url=self.baseurl, data=make_post_params.main(), files=files)
        return response

    def parse(self, file_name,file_dir):
        rsponse = self.post_response(file_name, file_dir)
        json = rsponse.json()
        if json['response_code'] == 0:
            print(Analyze_constant.response_code(0))
            print(json['data'])

        else:
            print(Analyze_constant.Verbose_Msg(json['verbose_msg']))
            exit()

    # 主函数方便调用
    def main(self, file_dir):
        # file_dir = '.\\'
        # 获取当前目录下的所有文件
        files = os.listdir(file_dir)
        # 遍历文件列表，输出文件名
        for file in files:
            self.parse(file, file_dir)

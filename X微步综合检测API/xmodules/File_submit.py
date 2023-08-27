'''
微步在线 提交文件分析
针对办公终端、Web/FTP/邮件附件等疑似恶意文件，
终端/服务器的可疑文件等，通过 22 款反病毒扫描引擎快速检测，
并根据不同文件类型，系统自动选择可运行的沙箱环境进行动态检测。
'''
import os
import requests


from xutils import make_post_params
from xutils import Analyze_constant


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
        # 获取当前目录下的所有文件
        # dirs为一个一维数组，包含路径下所有子目录名
        for root, dirs, files in os.walk(file_dir):
            # 遍历文件列表，传递目录下所有文件名和路径（包括子目录）
            for file in files:
                self.parse(file, root)

        # files = os.listdir(file_dir)

        # for file in files:
        #

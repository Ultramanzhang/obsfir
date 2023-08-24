#!/usr/bin/env python
# -*- coding: utf-8 -*-

from xmodules.IP_analyze import IpAnalyze

'''
本项目主类
'''


class X_api():
    def __init__(self):
        self.urls = []

    # 判断用户的使用方式
    def choose(self, choos):
        self.urls = []
        if choos == '1':
            self.urls.append(input("请输入待检测IP"))
            self.menu_choose()
        elif choos == '2':
            self.urls = self.redURL()
            self.menu_choose()
        else:
            print('输入有误，请重新确认您的输入！')
            self.main()

    # 用于处理批量的URL文本
    def redURL(self):
        with open('urls.txt', mode='r', encoding='utf8') as f:
            url = []
            ip = f.read().splitlines()
            for i in ip:
                url.append(i)
        return url

    # 菜单函数，可要可不要
    def menu(self):
        print('''
            _          __ _      
           | |        / _(_)     
       ___ | |__  ___| |_ _ _ __ 
      / _ \| '_ \/ __|  _| | '__|
     | (_) | |_) \__ \ | | | |   
      \___/|_.__/|___/_| |_|_|   
    感谢使用obsfir观火项目组，X微步API接口工具，为避免频繁请求，脚本为单线程版本，每次请求间隔在0.5-1s之间。
    ''')

    # 询问需用需要执行何种方法
    def menu_choose(self):
        choose = input('''请选择您想要执行的功能：\r\n1、IP分析\r\n2、IP荣誉''')
        if choose == '1':
            IpAnalyze.main(self.urls)

    # 类中的主函数，方便外部调用
    def main(self):
        self.choose(input('请输入工作模式\r\n1、单量检测\r\n2、批量检测'))


if __name__ == '__main__':
    x = X_api()
    x.menu()
    x.main()

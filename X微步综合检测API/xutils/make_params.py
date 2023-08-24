# -*- coding: utf-8 -*-
# make_params.py
'''
该脚本用于处理get请求中的数据
'''

from config_manager import ConfigManager

# 这两段函数用于读取config.yml的配置
config_manager = ConfigManager()
apitoken = config_manager.get_apitoken()


def main(ip):
    return {"apikey": apitoken, "resource": ip}

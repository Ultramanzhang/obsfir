'''
该脚本用于处理文件提交post请求中的数据
'''

from config_manager import ConfigManager

# 这两段函数用于读取config.yml的配置
config_manager = ConfigManager()
apitoken = config_manager.get_apitoken()


def main():
    return {"apikey": apitoken,  'sandbox_type': 'win7_sp1_enx86_office2013', 'run_time': 60}

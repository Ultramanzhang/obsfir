# config_manager.py
# -*- coding: utf-8 -*-

'''
配置文件统一管理工具，如果用户未填写则引导其填写
'''
import yaml


class ConfigManager:
    def __init__(self):
        self.config_file_path = '../config.yml'
        self.config = self._load_config()

    def _load_config(self):
        with open(self.config_file_path, 'r') as file:
            config = yaml.safe_load(file)
        return config

    def get_apitoken(self):
        if self.config().get('apikey') == '':
            self.config['apikey'] = input("请输入您的apikey：")
            with open(self.config_file_path, 'w') as file:
                yaml.dump(self.config['apikey'], file)
        else:
            return self.config().get('apikey')

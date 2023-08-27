import os

url = os.path.join(os.path.dirname(__file__), '..', 'config.yml')

# 处理yml文件
import yaml

with open(url, 'r') as file:
    config = yaml.safe_load(file)
    print(config['apikey'])


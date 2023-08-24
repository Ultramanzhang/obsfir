# X微步社区的API实现脚本
本脚本依据X微步的API文档编写，不涉及魔改等操作，方便在批量测试时的使用
- X微步在线API文档 https://x.threatbook.com/v5/apiDocs
- 当前项目架构如下：
```
│  urls.txt
│  result.txt
│  README.md
│
├─xmodules
│  │  IP_analyze.py
│  │  __init__.py
│  └─__pycache__
└─xutils
        Analyze_constant.py
        config_manager.py
        make_params.py
```
项目架构说明
```
confiog.yml---存放用户配置
result.txt---存放结构
urls.txt---存放待检测url
xmodules----存放主要实现脚本
xutils---存放本项目工具类
```


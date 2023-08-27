# -*- coding: utf-8 -*-
# Analyze_constant.py

'''
用于处理本项目中网页的返回数据对应值
'''


def response_code(code):
    response_codes = {
        0: "成功",
        1: "部分成功",
        2: "没有数据",
        3: "任务进行中",
        4: "未发现报告",
        5: "没有反病毒扫描引擎检测数据",
        6: "URL 下载文件失败",
        7: "URL 下载文件中",
        8: "URL 下载文件上传沙箱失败",
        -1: "权限受限或请求出错",
        -2: "请求无效",
        -3: "请求参数缺失",
        -4: "超出请求限制",
        -5: "系统错误"
    }
    return response_codes.get(code, "未知代码")


def Verbose_Msg(str):
    response_codes = {
        "Beyond Limitation from{IP/Domain}": "从某个IP或域名起超出请求次数限制。",
        "No Data": "没有数据。查询成功。查询的资源没有相关数据。",
        "In Progress": "任务进行中。报告正在生成中，请稍后查询。",
        "No Report Found": "未发现报告。请通过提交文件分析接口，重新提交文件并分析，再获取分析结果。",
        "No MultiEngines Data": "没有反病毒扫描引擎检测数据。请通过提交文件分析接口，重新提交文件并分析，再获取分析结果。",
        "URL Download Fail": "URL 下载文件失败。下载文件超时，请您重新提交扫描URL请求。",
        "URL Downloading": "URL 下载文件中。文件下载中，请稍等。一段时间内如仍无返回，请联系微步在线工作人员。",
        "URL Upload Sandbox Fail": "URL 下载文件上传沙箱失败。通过URL扫描报告获取文件SHA256值，前往s.threatbook.com，搜索该文件的SHA256，该文件即可自动提交到沙箱中。",
        "Invalid Account Status": "账户状态无效。您使用的API所属账户目前状态为无效。请联系微步在线工作人员。",
        "Invalid Access IP": "无效的访问IP。微步在线云API有访问IP白名单限制，请登录x.threatbook.com，点击右上角头像，进入'我的API'查看已绑定的IP与当前请求使用的IP是否一致。",
        "Invalid API Key": "无效的API key。请输入正确的APIKey。您的APIKey可通过登陆x.threatbook.com，点击右上角头像，进入'我的API'查询。",
    }
    return response_codes.get(str, "未知代码")


def judgments(str):
    judgments_code = {
        "C2": "远控",
        "Botnet": "僵尸网络",
        "Hijacked": "劫持",
        "Phishing": "钓鱼",
        "Malware": "恶意软件",
        "Exploit": "漏洞利用",
        "Scanner": "扫描",
        "Zombie": "傀儡机",
        "Spam": "垃圾邮件",
        "Suspicious": "可疑",
        "Compromised": "失陷主机",
        "Whitelist": "白名单",
        "Brute Force": "暴力破解",
        "Proxy": "代理",
        "Info": "基础信息",
        "MiningPool": "公共矿池",
        "CoinMiner": "私有矿池",
        "Suspicious Application": "潜在有害应用程序",
        "Suspicious Website": "潜在有害站点",
        "Reverse Proxy": "反向代理",
        "Fake Website": "仿冒网站",
        "Sinkhole C2": "安全机构接管 C2",
        "SSH Brute Force": "SSH暴力破解",
        "FTP Brute Force": "FTP暴力破解",
        "SMTP Brute Force": "SMTP暴力破解",
        "Http Brute Force": "HTTP AUTH暴力破解",
        "Web Login Brute Force": "撞库",
        "HTTP Proxy": "HTTP Proxy",
        "HTTP Proxy In": "HTTP代理入口",
        "HTTP Proxy Out": "HTTP代理出口",
        "Socks Proxy": "Socks代理",
        "Socks Proxy In": "Socks代理入口",
        "Socks Proxy Out": "Socks代理出口",
        "VPN": "VPN代理",
        "VPN In": "VPN入口",
        "VPN Out": "VPN出口",
        "Tor": "Tor代理",
        "Tor Proxy In": "Tor入口",
        "Tor Proxy Out": "Tor出口",
        "Bogon": "保留地址",
        "FullBogon": "未启用IP",
        "Gateway": "网关",
        "IDC": "IDC服务器",
        "Dynamic IP": "动态IP",
        "Edu": "教育",
        "DDNS": "动态域名",
        "Mobile": "移动基站",
        "Search Engine Crawler": "搜索引擎爬虫",
        "CDN": "CDN服务器",
        "Advertisement": "广告",
        "DNS": "DNS服务器",
        "BTtracker": "BT服务器",
        "Backbone": "骨干网",
        "ICP": "ICP备案",
        "IoT Device": "物联网设备",
        "Game Server": "游戏服务器"
    }
    return judgments_code.get(str, "未知代码")

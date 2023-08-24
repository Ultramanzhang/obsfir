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
# 通达OA sql注入漏洞
- 漏洞编号：CVE-2023-4166
- 影响版本：通达OA ≤ v11.10，v2017
该漏洞详情链接：https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-4166
> 修复链接：https://www.tongda2000.com/download/sp2022.php

该漏洞复现版本为 
TDOA11.9

脚本检测原理：
通过正常的payload与注入payload的服务器返回时间差值进行检测，由于本次漏洞采用时间盲注，通过两次访问得到的时间即可进行判定
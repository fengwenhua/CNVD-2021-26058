# yisaitong-rce-exp
亿赛通电子文档安全管理系统-rce-exp

## 漏洞成因
使用了Apache Solr，漏洞编号：CVE-2019-0193

## Fofa
```
"电子文档安全管理系统" && country!="CN"
```

## 脚本使用
```shell
~# python3 yisaitong.py -h
usage: yisaitong.py [-h] [-u URL] [-c CMD] [-f FILE]

亿赛通rce利用工具

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     指定单个url
  -c CMD, --cmd CMD     要执行的命令
  -f FILE, --file FILE  指定要测试的urls文件
```
